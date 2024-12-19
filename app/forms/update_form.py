from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import User



class UserUpdateForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    user = StringField("user", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
