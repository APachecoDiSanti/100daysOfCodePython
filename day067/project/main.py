from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os

from post_form import PostForm

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["WTF_CSRF_SECRET_KEY"] = os.urandom(32)
Bootstrap5(app)
CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    with app.app_context():
        posts = db.session.execute(db.select(BlogPost)).scalars().all()

    return render_template("index.html", all_posts=posts)


@app.route('/post/<post_id>')
def show_post(post_id):
    with app.app_context():
        requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    if request.method == "POST":
        with app.app_context():
            date_formatted = date.today().strftime("%B %d, %Y")
            post = BlogPost(
                title=request.form["title"],
                subtitle=request.form["subtitle"],
                date=date_formatted,
                body=request.form["body"],
                author=request.form["author"],
                img_url=request.form["img_url"]
            )
            db.session.add(post)
            db.session.commit()
        return redirect("/")
    else:
        form = PostForm()
        return render_template("make-post.html", form=form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        with app.app_context():
            post_data = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
            post_data.title = request.form["title"]
            post_data.subtitle = request.form["subtitle"]
            post_data.body = request.form["body"]
            post_data.author = request.form["author"]
            post_data.img_url = request.form["img_url"]
            db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    else:
        post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        form = PostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body,
        )
        return render_template("make-post.html", form=form, post=post)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<post_id>")
def delete_post(post_id):
    with app.app_context():
        post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        db.session.delete(post)
        db.session.commit()
        return redirect("/")

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
