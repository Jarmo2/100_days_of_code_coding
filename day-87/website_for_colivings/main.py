from flask import Flask, render_template, url_for, redirect, abort, flash, jsonify, request
from flask_bootstrap import Bootstrap
from forms import CreateColivingForm, RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from datetime import date
from flask_ckeditor import CKEditor
import random



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///colivings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ckeditor = CKEditor(app)
login_manager = LoginManager()
login_manager.init_app(app)


# to be defined
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## database tables
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = relationship("ColivingPost", back_populates="author")
    #comments = relationship("Comment", back_populates="comment_author")


class ColivingPost(db.Model):
    __tablename__ = "coliving_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    location = db.Column(db.String(500), unique=True, nullable=False)
    description_short = db.Column(db.String(250), nullable=False)
    description_long = db.Column(db.String(250), nullable=False)
    urbanlife = db.Column(db.String(250), nullable=False)
    changelocations = db.Column(db.String(250), nullable=False)
    coffee = db.Column(db.String(250), nullable=False)
    wifi = db.Column(db.String(250), nullable=False)
    sockets = db.Column(db.String(250), nullable=False)
    vibe = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
db.create_all()

@app.route('/')
def get_all_colivings():
    colivings = ColivingPost.query.all()
    return render_template("index.html", all_colivings=colivings, current_user=current_user)

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
            return redirect(url_for('get_all_colivings'))
    return render_template("login.html", form=form, current_user=current_user)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


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
        return redirect(url_for("get_all_colivings"))

    return render_template("register.html", form=form, current_user=current_user)



@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)

@app.route("/coliving/<int:coliving_id>", methods=["GET", "POST"])
def show_coliving(coliving_id):
    requested_coliving = ColivingPost.query.get(coliving_id)

    return render_template("post.html", coliving=requested_coliving, current_user=current_user)


@app.route("/edit-coliving/<int:coliving_id>", methods=["GET", "POST"])
@admin_only
@login_required
def edit_coliving(coliving_id):
    entry = ColivingPost.query.get(coliving_id)
    edit_form = CreateColivingForm(
        title=entry.title,
        location=entry.location,
        description_short=entry.description_short,
        description_long=entry.description_long,
        urbanlife=entry.urbanlife,
        changelocations=entry.changelocations,
        wifi=entry.wifi,
        coffee=entry.coffee,
        sockets=entry.sockets,
        vibe=entry.vibe,
        author=current_user,
        img_url=entry.img_url,
    )

    if edit_form.validate_on_submit():
        entry.title = edit_form.title.data
        entry.location = edit_form.location.data
        entry.description_short = edit_form.description_short.data
        entry.description_long = edit_form.description_long.data
        entry.urbanlife = edit_form.urbanlife.data
        entry.changelocations = edit_form.changelocations.data
        entry.wifi = edit_form.wifi.data
        entry.coffee = edit_form.coffee.data
        entry.sockets = edit_form.sockets.data
        entry.vibe = edit_form.vibe.data
        entry.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_coliving", coliving_id=entry.id))

    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_colivings'))


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_coliving():
    form = CreateColivingForm()
    if form.validate_on_submit():
        new_post = ColivingPost(
            title=form.title.data,
            location=form.location.data,
            description_short=form.description_short.data,
            description_long=form.description_long.data,
            urbanlife=form.urbanlife.data,
            changelocations=form.changelocations.data,
            wifi=form.wifi.data,
            coffee=form.coffee.data,
            sockets=form.sockets.data,
            vibe=form.vibe.data,
            author=current_user,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_colivings"))

    return render_template("make-post.html", form=form, current_user=current_user)

@app.route("/delete/<int:coliving_id>")
@admin_only
def delete_coliving(coliving_id):
    post_to_delete = ColivingPost.query.get(coliving_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_colivings'))

#APIs
@app.route('/api/info')
def explain_the_api():
    colivings = ColivingPost.query.all()
    return render_template("api.html", all_colivings=colivings, current_user=current_user)


@app.route("/API/random")
def API_random_coliving():
    colivings = ColivingPost.query.all()
    random_coliving = random.choice(colivings)
    return jsonify(cafe=random_coliving.to_dict())


@app.route("/API/all")
def API_all_colivings():
    colivings = ColivingPost.query.all()
    return jsonify(cafes=[coliving.to_dict() for coliving in colivings])


@app.route("/API/search")
def get_cafe_at_location():
    coliving_name = request.args.get("loc")
    coliving = db.session.query(ColivingPost).filter_by(title=coliving_name).first()
    if coliving:
        return jsonify(coliving=coliving.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

#@app.route("/API/search")
#def get_cafe_at_location():


if __name__ == '__main__':
    app.run(debug=True)

