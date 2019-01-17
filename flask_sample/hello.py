from flask import Blueprint, render_template

hello = Blueprint('hello', __name__, template_folder='templates')


@hello.route('/')
def index():
    return render_template('index.html')
