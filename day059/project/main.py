from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_blog_posts():
    response = requests.get("https://api.npoint.io/46f81f6554bf05abac9e")
    response.raise_for_status()
    return response.json()


@app.route("/")
@app.route("/home")
def home():
    blog_posts = get_blog_posts()
    return render_template("index.html", head_img="home-bg.jpg", blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html", head_img="about-bg.jpg")


@app.route("/contact")
def contact():
    return render_template("contact.html", head_img="contact-bg.jpg")


@app.route("/post/<post_id>")
def post(post_id):
    blog_posts = get_blog_posts()
    post_data = blog_posts[int(post_id)-1]
    return render_template("post.html", post_data=post_data, head_img=f"{post_id}-bg.jpg")


if __name__ == "__main__":
    app.run(debug=True)
