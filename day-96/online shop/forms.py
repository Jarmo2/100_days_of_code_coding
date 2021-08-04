from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired



##WTForm

class RegisterForm(FlaskForm):
    first_n = StringField("first name", validators=[DataRequired()])
    last_n = StringField("last name", validators=[DataRequired()])
    s_and_n = StringField("Street and house number", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    zip_code = StringField("zip code", validators=[DataRequired()])
    email = StringField("e-mail", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")
