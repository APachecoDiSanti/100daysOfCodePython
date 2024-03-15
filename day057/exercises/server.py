from flask import Flask, render_template
from datetime import datetime

import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=datetime.now().year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get("https://api.genderize.io", params={"name": name})
    response.raise_for_status()
    gender = response.json()["gender"]

    response = requests.get("https://api.agify.io", params={"name": name})
    response.raise_for_status()
    age = response.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<blog_id>")
def blog(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    posts = response.json()
    return render_template("blog.html", posts=posts, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
