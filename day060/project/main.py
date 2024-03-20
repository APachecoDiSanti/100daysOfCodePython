from flask import Flask, render_template, request

from email.mime.text import MIMEText
import os
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        receive_data()
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    print(f"""Name: {name}
Email: {email}
Phone: {phone}
Message: {message}    
""")


def send_email(content):
    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = "Contact Form"
    msg['From'] = EMAIL_FROM

    print(f"Connecting to {SMTP_HOST}:{SMTP_PORT}")
    with smtplib.SMTP(host=SMTP_HOST, port=int(SMTP_PORT)) as connection:
        print(f"Sending email to {EMAIL_TO}...")
        connection.sendmail(from_addr=EMAIL_FROM, to_addrs=[EMAIL_TO], msg=msg.as_string())
        print("Email sent!")
        connection.close()


if __name__ == "__main__":
    SMTP_HOST = os.environ["SMTP_HOST"]
    SMTP_PORT = os.environ["SMTP_PORT"]
    EMAIL_FROM = os.environ["EMAIL_FROM"]
    EMAIL_TO = os.environ["EMAIL_TO"]
    app.run(debug=True, port=5001)
