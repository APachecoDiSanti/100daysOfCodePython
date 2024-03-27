from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
        print(type(all_books))
        print(all_books)
        return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            db.session.add(
                Book(
                    title=request.form.get("title"),
                    author=request.form.get("author"),
                    rating=request.form.get("rating"),
                )
            )
            db.session.commit()
            return redirect("/")
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        with app.app_context():
            book_id = int(request.form["book_id"])
            book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            book.rating = float(request.form["new_rating"])
            db.session.commit()
            return redirect("/")
    else:
        book_id = request.args.get("id")
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        return render_template("edit.html", book=book)


@app.route("/delete", methods=["GET"])
def delete():
    with app.app_context():
        book_id = request.args.get("id")
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book)
        db.session.commit()
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

