from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL


class ToDo(FlaskForm):
    todo = StringField(validators=[DataRequired()], default="Please type your todo here.")
    comment = StringField('Your comments/details')
    priority = SelectField('Please determine the priority', choices=["🔥🔥🔥", "🔥🔥", "🔥"])
    submit = SubmitField('put me on the list')


    #create a separate form for the todo list list
class SelectTodo(FlaskForm):
    select_todo = SelectField('Please select your todo', choices=['Nothing yet defined'])
    wip = SubmitField('Make me WIP')
    change = SubmitField('Correct Me')


class WIP(FlaskForm):
    select_wip = SelectField('WIP', choices=['Nothing yet defined'])
    to_todo = SubmitField('Send me back to do')
    done = SubmitField('Make me done')


class Done(FlaskForm):
    select_done = SelectField('Done', choices=['Nothing yet defined'])
    wip = SubmitField('Make me wip')
    delete = SubmitField('Delete me')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")





