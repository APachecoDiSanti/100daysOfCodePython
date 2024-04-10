from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from werkzeug.exceptions import NotFound

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random_cafe():
    with app.app_context():
        number_of_cafes = db.session.query(Cafe).count()
        random_id = random.randint(1, number_of_cafes)
        cafe_data = db.session.execute(db.select(Cafe).where(Cafe.id == random_id)).scalar()

    return jsonify(
        cafe=cafe_to_dict(cafe_data)
    )


def cafe_to_dict(cafe):
    return {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }


@app.route("/all", methods=["GET"])
def all_cafes():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        print(type(cafes))
        print(cafes)
        cafe_list = [cafe_to_dict(cafe) for cafe in cafes]

    return jsonify(cafes=cafe_list)


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("loc")

    with app.app_context():
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
        cafe_list = [cafe_to_dict(cafe) for cafe in cafes]

    if cafe_list:
        return jsonify(cafes=cafe_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at the location."})


@app.route("/add", methods=["POST"])
def add():
    with app.app_context():
        cafe = Cafe(
            name=request.form["name"],
            map_url=request.form["map_url"],
            img_url=request.form["img_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            has_toilet=bool(request.form["has_toilet"]),
            has_wifi=bool(request.form["has_wifi"]),
            has_sockets=bool(request.form["has_sockets"]),
            can_take_calls=bool(request.form["can_take_calls"]),
            coffee_price=request.form["coffee_price"]
        )
        db.session.add(cafe)
        db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        new_price = request.args.get("new_price")

        with app.app_context():
            cafe = db.get_or_404(Cafe, cafe_id)
            cafe.coffee_price = new_price
            db.session.commit()

        return jsonify(response={"success": "Successfully update the price."})
    except NotFound:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."})


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    try:
        api_key = request.args.get("api-key")
        if api_key != "TopSecretAPIKey":
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")
        else:
            with app.app_context():
                cafe = db.get_or_404(Cafe, cafe_id)
                db.session.delete(cafe)
                db.session.commit()

            return jsonify(response={"success": "Successfully deleted the cafe."})
    except NotFound:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."})


if __name__ == '__main__':
    app.run(debug=True)
