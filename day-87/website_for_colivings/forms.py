from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL


class CreateColivingForm(FlaskForm):
    title = StringField('Coliving Name', validators=[DataRequired()])
    location = StringField('Coliving location on OpenStreetMap (HTML code)', validators=[DataRequired()])
    description_short = StringField('Short description', validators=[DataRequired()])
    description_long = StringField('Long description', validators=[DataRequired()])
    urbanlife = SelectField('Urban life', choices=["🏙️", "🏙️🏙️", "🏙️🏙️🏙️", "🏙️🏙️🏙️🏙️", "🏙️🏙️🏙️🏙️🏙️"], validators=[DataRequired()])
    changelocations = SelectField('Change your workplace', choices=["🚶‍♀️", "🚶‍♀️🚶‍♀️", "🚶‍♀️🚶‍♀️🚶‍♀️", "🚶‍♀️🚶‍♀️🚶‍♀️🚶‍♀️", "🚶‍♀️🚶‍♀️🚶‍♀️🚶‍♀️🚶‍♀️"], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength', choices=["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    sockets = SelectField('Number of sockets', choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    vibe = SelectField('Community', choices=["💬", "💬💬", "💬💬💬", "💬💬💬💬", "💬💬💬💬💬"], validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")