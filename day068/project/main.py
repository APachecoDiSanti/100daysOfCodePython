from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


SALT_LENGTH = 8

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['UPLOAD_FOLDER'] = 'static/files'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        with app.app_context():
            user_name = request.form["name"]
            existing_user = db.session.execute(db.select(User).where(User.email == request.form["email"])).scalar()
            if existing_user:
                flash("A user with that email already exists.")
                return redirect(url_for("register"))

            user = User(
                name=user_name,
                email=request.form["email"],
                password=generate_password_hash(
                    request.form["password"],
                    method="pbkdf2:sha256",
                    salt_length=SALT_LENGTH
                )
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
        return redirect(url_for("secrets"))
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        with app.app_context():
            email = request.form["email"]
            user = db.session.execute(db.select(User).where(User.email == email)).scalar()
            if not user:
                flash("Wrong email. Try again.")
                return redirect(url_for("login"))
            if not check_password_hash(user.password, request.form["password"]):
                flash("Wrong password/email combination. Try again.")
                return redirect(url_for("login"))
            login_user(user)
            flash('Logged in successfully.')
            next_arg = request.args.get('next')  # how to check this?
            return redirect(url_for("secrets"))

    else:
        return render_template("login.html", login_manager=login_manager)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
