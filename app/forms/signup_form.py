from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import King  # Changed from User to King


def user_exists(_form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError("Email address is already in use.")


def username_exists(_form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.user == username).first()
    if user:
        raise ValidationError("Username is already in use.")


class SignUpForm(FlaskForm):
    user = StringField(
        "user", validators=[DataRequired(), username_exists]
    )
    email = StringField(
        "email", validators=[DataRequired(), user_exists]
    )
    password = StringField("password", validators=[DataRequired()])
