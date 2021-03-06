from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL


class CreateColivingForm(FlaskForm):
    title = StringField('Coliving Name', validators=[DataRequired()])
    location = StringField('Coliving location on OpenStreetMap (HTML code)', validators=[DataRequired()])
    description_short = StringField('Short description', validators=[DataRequired()])
    description_long = StringField('Long description', validators=[DataRequired()])
    urbanlife = SelectField('Urban life', choices=["ποΈ", "ποΈποΈ", "ποΈποΈποΈ", "ποΈποΈποΈποΈ", "ποΈποΈποΈποΈποΈ"], validators=[DataRequired()])
    changelocations = SelectField('Change your workplace', choices=["πΆββοΈ", "πΆββοΈπΆββοΈ", "πΆββοΈπΆββοΈπΆββοΈ", "πΆββοΈπΆββοΈπΆββοΈπΆββοΈ", "πΆββοΈπΆββοΈπΆββοΈπΆββοΈπΆββοΈ"], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength', choices=["πͺ", "πͺπͺ", "πͺπͺπͺ", "πͺπͺπͺπͺ", "πͺπͺπͺπͺπͺ"], validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=["β", "ββ", "βββ", "ββββ", "βββββ"], validators=[DataRequired()])
    sockets = SelectField('Number of sockets', choices=["π", "ππ", "πππ", "ππππ", "πππππ"], validators=[DataRequired()])
    vibe = SelectField('Community', choices=["π¬", "π¬π¬", "π¬π¬π¬", "π¬π¬π¬π¬", "π¬π¬π¬π¬π¬"], validators=[DataRequired()])
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