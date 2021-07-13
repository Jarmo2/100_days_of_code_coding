from flask import Flask, render_template, flash, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from forms import ToDo, WIP, Done, RegisterForm, LoginForm, SelectTodo
from flask_login import UserMixin, LoginManager, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    todo = relationship("TodoPost", back_populates="author")
    wip = relationship("WIPPost", back_populates="author")
    done = relationship("DonePost", back_populates="author")


class TodoPost(db.Model):
    __tablename__ = "todo_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="todo")
    date = db.Column(db.String(250), nullable=False)
    item = db.Column(db.String(250), unique=False, nullable=True)
    comment = db.Column(db.String(250), unique=False, nullable=True)
    priority = db.Column(db.String(250), unique=False, nullable=True)

class WIPPost(db.Model):
    __tablename__ = "wip_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="wip")
    date = db.Column(db.String(250), nullable=False)
    item = db.Column(db.String(250), unique=False, nullable=True)
    comment = db.Column(db.String(250), unique=False, nullable=True)
    priority = db.Column(db.String(250), unique=False, nullable=True)


class DonePost(db.Model):
    __tablename__ = "done_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="done")
    date = db.Column(db.String(250), nullable=False)
    item = db.Column(db.String(250), unique=False, nullable=True)
    comment = db.Column(db.String(250), unique=False, nullable=True)
    priority = db.Column(db.String(250), unique=False, nullable=True)


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#add login requirement
@app.route('/', methods=["GET", "POST"])
def todo():
    form = ToDo()
    form_select = SelectTodo()
    wip_form = WIP()
    done_form = Done()
    form_select.select_todo.choices = [todo.item for todo in TodoPost.query.all()]
    wip_form.select_wip.choices = [wip.item for wip in WIPPost.query.all()]
    done_form.select_done.choices = [done.item for done in DonePost.query.all()]


    if form.validate_on_submit() and form.todo.data != "Please type your todo here." and form.todo.data:
        new_todo = TodoPost(
            item=form.todo.data,
            date=date.today().strftime("%B %d, %Y"),
            comment=form.comment.data,
            priority=form.priority.data,
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('todo'))

    if form_select.validate_on_submit() and form_select.change.data:
        chosen = form_select.select_todo.data
        TodoPost.query.filter_by(item=chosen).delete()
        db.session.commit()
        return redirect(url_for("todo"))

    if form_select.validate_on_submit() and form_select.wip.data:
        chosen = form_select.select_todo.data
        chosen_in_db = [(new_wip.item, new_wip.priority, new_wip.comment) for new_wip in
                        TodoPost.query.filter_by(item=chosen).all()]
        to_wip = WIPPost(
            item=chosen_in_db[0][0],
            date=date.today().strftime("%B %d, %Y"),
            comment=chosen_in_db[0][2],
            priority=chosen_in_db[0][1],
        )
        TodoPost.query.filter_by(item=chosen).delete()
        db.session.add(to_wip)
        db.session.commit()
        return redirect(url_for("todo"))

    if wip_form.validate_on_submit() and wip_form.to_todo.data:
        chosen = wip_form.select_wip.data
        chosen_in_db = [(update_todo.item, update_todo.priority, update_todo.comment) for update_todo in
                        WIPPost.query.filter_by(item=chosen).all()]
        again_todo = TodoPost(
            item=chosen_in_db[0][0],
            date=date.today().strftime("%B %d, %Y"),
            comment=chosen_in_db[0][2],
            priority=chosen_in_db[0][1],
        )
        WIPPost.query.filter_by(item=chosen).delete()
        db.session.add(again_todo)
        db.session.commit()
        return redirect(url_for("todo"))

    if wip_form.validate_on_submit() and wip_form.done.data:
        chosen = wip_form.select_wip.data
        chosen_in_db = [(new_done.item, new_done.priority, new_done.comment) for new_done in WIPPost.query.filter_by(item=chosen).all()]
        new_done = DonePost(
            item=chosen_in_db[0][0],
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
            comment=chosen_in_db[0][2],
            priority=chosen_in_db[0][1],
        )
        WIPPost.query.filter_by(item=chosen).delete()
        db.session.add(new_done)
        db.session.commit()
        return redirect(url_for("todo"))

    if done_form.validate_on_submit() and done_form.delete.data:
        chosen = done_form.select_done.data
        DonePost.query.filter_by(item=chosen).delete()
        db.session.commit()
        return redirect(url_for("todo"))

    if done_form.validate_on_submit() and done_form.wip.data:
        chosen = done_form.select_done.data
        chosen_in_db = [(done.item, done.priority, done.comment) for done in
                        DonePost.query.filter_by(item=chosen).all()]
        wip_again = WIPPost(
            item=chosen_in_db[0][0],
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
            comment=chosen_in_db[0][2],
            priority=chosen_in_db[0][1],
        )
        DonePost.query.filter_by(item=chosen).delete()
        db.session.add(wip_again)
        db.session.commit()
        return redirect(url_for("todo"))

    return render_template("index.html", form=form, form_select=form_select, wip_form=wip_form, done_form=done_form)

@app.route('/todo/<id>')
def todo_to_wip(id):
    todos = TodoPost.query.all()

    todoArray = []

    for todo in todos:
        todoObj = {}
        todoObj['id'] = todo.id
        todoObj['name'] = todo.item
        todoArray.append(todoObj)

    return jsonify({'todos': todoArray})

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('todo'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            print(User.query.filter_by(email=form.email.data).first())
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("todo"))

    return render_template("register.html", form=form, current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)