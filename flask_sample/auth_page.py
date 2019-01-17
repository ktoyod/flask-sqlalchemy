from flask import Blueprint, render_template

auth_page = Blueprint('auth_page', __name__, url_prefix='/auth', template_folder='templates')


@auth_page.route('/register')
def register():
    return render_template('auth/register.html')


@auth_page.route('/login')
def login():
    return render_template('auth/login.html')
