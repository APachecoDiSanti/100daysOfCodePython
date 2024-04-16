from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, DateField, URLField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    img_url = URLField(label='Image URL', validators=[DataRequired()])
    body = CKEditorField(label='Body', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
