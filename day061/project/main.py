import os

from flask import Flask, render_template, redirect
from login_form import LoginForm
from flask_bootstrap import Bootstrap5


SECRET_SIZE = 32

app = Flask(__name__)
app.config.update({
    "SECRET_KEY": os.urandom(SECRET_SIZE),
    "WTF_CSRF_SECRET_KEY": os.urandom(SECRET_SIZE)
})

bootstrap = Bootstrap5(app)


# @app.route("/login")
# def login():
#     return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect("/success")
        else:
            return redirect("/denied")
    return render_template("login.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
