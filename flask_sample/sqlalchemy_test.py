import json
from flask import Blueprint, render_template, request

from flask_sample import models
from flask_sample.database import db

sqlalchemy_test = Blueprint('sqlalchemy_test',
                            __name__,
                            url_prefix='/sqlalchemy_test',
                            template_folder='templates')


@sqlalchemy_test.route('/')
def index():
    return render_template('sqlalchemy_test/index.html')


@sqlalchemy_test.route('add_user_page', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']

    user = models.User()
    user.name = name
    user.age = age

    db.session.add(user)
    db.session.commit()

    users = db.session.query(models.User).all()
    users_dict = {}
    for user in users:
        users_dict[user.id] = {'name': user.name,
                               'age': user.age,
                               }
    return json.dumps(users_dict)


@sqlalchemy_test.route('add_post_page', methods=['POST'])
def add_post():
    title = request.form['title']
    article = request.form['article']

    post = models.Post()
    post.title = title
    post.article = article

    db.session.add(post)
    db.session.commit()

    posts = db.session.query(models.Post).all()
    posts_dict = {}
    for post in posts:
        posts_dict[post.id] = {'title': post.title,
                               'article': post.article,
                               }
    return json.dumps(posts_dict)
