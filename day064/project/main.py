from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

from movie_form import MovieForm, AddMovieForm

import os
import requests


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
TMDB_API_KEY = os.environ["TMDB_API_KEY"]
TMDB_API_READ_AT = os.environ["TMDB_API_READ_AT"]
TMDB_BASE_URL = "https://api.themoviedb.org/3"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["WTF_CSRF_SECRET_KEY"] = os.urandom(32)
db.init_app(app)

with app.app_context():
    db.create_all()

Bootstrap5(app)

# CREATE DB


# CREATE TABLE


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
        movies = result.scalars().all()

        for i in range(0, len(movies)):
            movies[i].ranking = i+1

        return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        with app.app_context():
            movie_id = request.args.get("id")
            movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            movie.rating = float(request.form["new_rating"])
            movie.review = request.form["new_review"]
            db.session.commit()
            return redirect("/")
    else:
        form = MovieForm()
        movie_id = request.args.get("id")
        movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["GET"])
def delete():
    with app.app_context():
        movie_id = request.args.get("id")
        movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie)
        db.session.commit()
        return redirect("/")


@app.route('/add', methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form["title"]

        response = requests.get(
            url=f"{TMDB_BASE_URL}/search/movie?query={title}&include_adult=false&language=en-US&page=1",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {TMDB_API_READ_AT}"
            }
        )
        response.raise_for_status()
        movies = response.json()["results"]

        return render_template("select.html", movies=movies)
    else:
        form = AddMovieForm()
        return render_template("add.html", form=form)


@app.route("/add-details")
def add_details():
    with app.app_context():
        tmdb_movie_id = request.args.get("id")

        response = requests.get(
            url=f"{TMDB_BASE_URL}/movie/{tmdb_movie_id}",
            params={
                "language": "en-US"
            },
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {TMDB_API_READ_AT}"
            }
        )
        response.raise_for_status()
        details = response.json()

        with app.app_context():
            movie = Movie(
                    title=details["title"],
                    year=details["release_date"].split("-")[0],
                    description=details["overview"],
                    rating=0.0,
                    ranking=0,
                    review="",
                    img_url=f"""https://media.themoviedb.org/t/p/w300_and_h450_bestv2{details["poster_path"]}"""
                )
            db.session.add(movie)
            db.session.commit()
            return redirect(f"/edit?id={movie.id}")


if __name__ == "__main__":
    app.run(debug=True)
