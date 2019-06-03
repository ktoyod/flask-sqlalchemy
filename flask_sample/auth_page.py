import crypt
from hmac import compare_digest
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from flask_sample import models
from flask_sample.database import db

auth_page = Blueprint('auth_page', __name__, url_prefix='/auth', template_folder='templates')


@auth_page.route('/')
@login_required
def index():
    return render_template('auth/index.html')


@auth_page.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        user = models.User()
        user.name = request.form['username']
        user.email = request.form['email']
        user.age = request.form['age']
        salt = crypt.mksalt(crypt.METHOD_SHA512)
        user.salt = salt
        hashed_password = crypt.crypt(request.form['password'], salt)
        user.password = hashed_password
        db.session.add(user)
        db.session.commit()
        return render_template('auth/login.html')


@auth_page.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    if request.method == 'POST':
        user = models.User.query.get(request.form['user_id'])
        if user:
            if compare_digest(crypt.crypt(request.form['Password'], user.salt), user.password):
                user.authetiacted = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('auth_page.index'))
            else:
                return render_template('auth/login.html', message='invalid password')
        else:
            return render_template('auth/login.html', message='user not exist')
    return render_template('auth/login.html')  # , form=form)


@auth_page.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('auth/login.html')
