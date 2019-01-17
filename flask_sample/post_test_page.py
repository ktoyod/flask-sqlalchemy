import json
from flask import Blueprint, render_template, request

post_test_page = Blueprint('post_test_page',
                           __name__,
                           url_prefix='/post_test',
                           template_folder='templates')


@post_test_page.route('/')
def index():
    return render_template('post_test/index.html')


@post_test_page.route('/post_test', methods=['POST'])
def post_test():
    name = request.form['name']
    age = request.form['age']

    return render_template('post_test/post_test.html', name=name, age=age)


@post_test_page.route('/post_test.json', methods=['POST'])
def post_json():
    name = request.form['name']
    age = request.form['age']

    return json.dumps({'success': True, 'name': name, 'age': age})
