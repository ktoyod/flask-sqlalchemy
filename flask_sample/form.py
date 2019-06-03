from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('Usernmae')
    password = PasswordField('Password')
    id = StringField('id')
    submit = SubmitField('Submit')
