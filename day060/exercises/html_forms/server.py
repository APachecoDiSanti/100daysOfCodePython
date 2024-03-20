from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["name"]
    password = request.form["password"]
    return f"<h1>{name}</h1><h2>{password}</h2>"


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
