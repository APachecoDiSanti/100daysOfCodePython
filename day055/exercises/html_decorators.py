from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def b():
        text = function()
        return f"<b>{text}</b>"
    return b


def make_underlined(function):
    def u():
        text = function()
        return f"<u>{text}</u>"
    return u


def make_itallic(function):
    def i():
        text = function()
        return f"<i>{text}</i>"
    return i


@app.route("/bye")
@make_bold
@make_underlined
@make_itallic
def bye():
    return "Bye!"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
