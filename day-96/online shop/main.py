from flask import Flask, render_template, flash, redirect, url_for, request, session
from forms import LoginForm, RegisterForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship

#Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class Customer(UserMixin, db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zip_code = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    sessions = relationship("DogSurfSessions", back_populates="customer")


class DogSurfSessions(db.Model):
    __tablename__ = "booked_sesssions"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="sessions")
    date = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    paid = db.Column(db.Boolean(1), nullable=True)
db.create_all()


@app.route('/')
def show_home():
    return render_template("index.html", current_page="Pricing")

@app.route('/login', methods=["GET", "POST"])
def show_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = "Hans"
        #user = User.query.filter_by(email=email).first()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            #login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_page="Login", current_user="Peter") #current_user=current_user)

@app.route('/register', methods=["GET", "POST"])
def show_register():
    form = RegisterForm()
    return render_template("register.html", current_page="Register", form=form, current_user='current_user')


@app.route('/date_time/<plan>', methods=["GET", "POST"])
def show_date(plan):
    session['plan'] = plan

    if plan == "cheap":
        chosen_product = "Street Dog"
        chosen_product_desc = "the cheap fella plan"
        price = "€ 10"
        return render_template("date_time.html", current_page="Finalise your order here", chosen_product=chosen_product,
                               chosen_product_desc=chosen_product_desc, price=price)

    elif plan == "medium":
        chosen_product = "Guard Dog"
        chosen_product_desc = "the wallflower plan"
        price = "€ 20"
        return render_template("date_time.html", current_page="Finalise your order here", chosen_product=chosen_product,
                               chosen_product_desc=chosen_product_desc, price=price)

    elif plan == "expensive":
        chosen_product = "Lap Dog"
        chosen_product_desc = "the Donald plan"
        price = "€ 60"
        return render_template("date_time.html", current_page="Finalise your order here", chosen_product=chosen_product,
                               chosen_product_desc=chosen_product_desc, price=price)



@app.route('/sessions', methods=['POST', 'GET'])
def show_sessions():

    if request.method == 'POST':
        new_user = Customer(
            email=request.form.get('email'),
            first_name=request.form.get('firstname'),
            last_name=request.form.get('lastname'),
            street=request.form.get('address'),
            city=request.form.get('city'),
            zip_code=request.form.get('zip'),
            phone=request.form.get('phone'),
        )
        db.session.add(new_user)
        db.session.commit()

        new_session = DogSurfSessions(
            date=request.form.get('date'),
            type=session['plan']
        )
        db.session.add(new_session)
        db.session.commit()

        if session['plan'] == "cheap":
            return redirect("https://test.adyen.link/PLB99DD2CF895FEBFD")

        elif session['plan'] == "medium":
            return redirect("https://test.adyen.link/PLCB5565054EEC6400")
        elif session['plan'] == "expensive":
            return redirect('https://test.adyen.link/PLC1FE9CB97CBFE9AA')

    return render_template("session.html", current_page="Your sessions")

@app.route('/checkout', methods=["GET", "POST"])
def show_checkout():
    return render_template("checkout.html")


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

