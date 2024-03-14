from flask import *

app = Flask(__name__)


@app.route("/")
def serve_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
