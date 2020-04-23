from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=5, max=15)])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=8, max=100)])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email/Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")