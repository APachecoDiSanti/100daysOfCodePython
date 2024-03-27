from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MovieForm(FlaskForm):
    new_rating = StringField(label="Your rating out of 10 (e.g.: 7.5)", validators=[DataRequired(), NumberRange(min=1, max=10)])
    new_review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Update movie")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add movie")
