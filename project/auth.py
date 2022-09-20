from flask import Blueprint, render_template,redirect,flash
from .forms import loginForm,registerForm
from .models import User
from flask_login import login_user,logout_user,login_required
from werkzeug.security  import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():    
    login_Form = loginForm()
    if login_Form.validate():
        password = login_Form.password.data
        user = User.query.filter_by(email=login_Form.email.data).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user, remember=True)
                flash("You are logged in.",category="success")
                return redirect('/')
            else:
                flash("Incorrect password!!",category="danger")
        else:
            flash("This E-mail not registered.",category="danger") 
    return render_template('login.html',form=login_Form, search=False)


@auth.route('/register',methods=['GET','POST'])
def register():
    register_form= registerForm()

    if register_form.validate():
        email =register_form.email.data 
        password = register_form.password.data
        conf_pass =register_form.conf_password.data  

        print(email,password,conf_pass)

        user = User.query.filter_by(email=email).first()
        print(user)

        if user:
             flash("Email already registered.",category="danger")
        else:    
            if password==conf_pass:
                user = User(email=email, password= generate_password_hash(password,method='sha256'))
                db.session.add(user)
                db.session.commit()
                flash("Registeration successfull, You are logged in.",category="success")
                login_user(user,remember=True)
                return redirect('/')
            else: 
                flash("Passwords do not match! please try again.",category="warning")
                  

    return render_template('register.html',form=register_form, search=False)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return  redirect('/login')


