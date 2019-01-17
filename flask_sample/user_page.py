from flask import Blueprint

user_page = Blueprint('user', __name__, url_prefix='/user')


@user_page.route('/<username>')
def profile(username):
    return f'Hello, {username}!'


@user_page.route('/user_age/<age>')
def user_age(age):
    return f'You are {age} years old.'
