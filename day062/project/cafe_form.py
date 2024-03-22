from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    name = StringField(label="Cafe Name", validators=[DataRequired()])
    location = URLField(label="Location", validators=[DataRequired()])
    open_time = TimeField(label="Open", validators=[DataRequired()])
    close_time = TimeField(label="Close", validators=[DataRequired()])
    coffee_lvl = SelectField(
        label="Coffee",
        choices=[
            "✘",
            "☕",
            "☕☕",
            "☕☕☕",
            "☕☕☕☕",
            "☕☕☕☕☕"
        ],
        validators=[DataRequired()]
    )
    wifi_lvl = SelectField(
        label="WiFi",
        choices=[
            "✘",
            "💪",
            "💪💪",
            "💪💪💪",
            "💪💪💪💪",
            "💪💪💪💪💪"
        ],
        validators=[DataRequired()]
    )
    power_lvl = SelectField(
        label="Power",
        choices=[
            "✘",
            "🔌",
            "🔌🔌",
            "🔌🔌🔌",
            "🔌🔌🔌🔌",
            "🔌🔌🔌🔌🔌"
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add Cafe")
