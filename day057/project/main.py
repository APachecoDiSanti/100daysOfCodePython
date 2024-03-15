from flask import Flask, render_template
from post import Post

import requests


app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    post_dicts = response.json()
    posts = [Post(post_dict) for post_dict in post_dicts]
    return render_template("index.html", posts=posts)


@app.route("/post/<post_id>")
def read(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    post_dict = response.json()[int(post_id)-1]
    post = Post(post_dict)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
