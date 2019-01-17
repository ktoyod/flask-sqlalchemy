import datetime
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


@sqlalchemy_test.route('/add_user_page', methods=['POST'])
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
                               'created_at': user.created_at,
                               'updated_at': user.updated_at
                               }
    return json.dumps(users_dict, default=json_serial)


@sqlalchemy_test.route('/add_post_page', methods=['POST'])
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
                               'created_at': post.created_at,
                               'updated_at': post.updated_at
                               }
    return json.dumps(posts_dict, default=json_serial)


@sqlalchemy_test.route('/user_id/<int:id>')
def get_user_by_id(id):
    user = models.User.query.filter_by(id=id).first()

    user_dict = {'id': user.id,
                 'name': user.name,
                 'age': user.age,
                 'created_at': user.created_at,
                 'updated_at': user.updated_at
                 }
    return json.dumps(user_dict, default=json_serial)


@sqlalchemy_test.route('/users_by_id', methods=['POST'])
def get_users_by_id():
    ids = request.form['ids']
    ids_tuple = tuple(ids.split(','))
    users = models.User.query.filter(models.User.id.in_(ids_tuple)).all()

    users_dict = {}
    for user in users:
        users_dict[user.id] = {'name': user.name,
                               'age': user.age,
                               'created_at': user.created_at,
                               'updated_at': user.updated_at
                               }
    return json.dumps(users_dict, default=json_serial)


@sqlalchemy_test.route('/updated_record', methods=['POST'])
def update_record_by_id():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']

    user = models.User.query.filter_by(id=id).first()
    user.name = name if name else user.name
    user.age = age if age else user.age
    db.session.add(user)
    db.session.commit()

    user = models.User.query.filter_by(id=id).first()

    user_dict = {'id': user.id,
                 'name': user.name,
                 'age': user.age,
                 'created_at': user.created_at,
                 'updated_at': user.updated_at
                 }
    return json.dumps(user_dict, default=json_serial)


@sqlalchemy_test.route('/deleted_record', methods=['POST'])
def delete_record_by_id():
    id = request.form['id']

    user = models.User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return get_all_users()


@sqlalchemy_test.route('/all_users')
def get_all_users():
    users = db.session.query(models.User).all()
    users_dict = {}
    for user in users:
        users_dict[user.id] = {'name': user.name,
                               'age': user.age,
                               'created_at': user.created_at,
                               'updated_at': user.updated_at
                               }
    return json.dumps(users_dict, default=json_serial)


@sqlalchemy_test.route('/time_in/<int:minutes>')
def get_user_in_time(minutes):
    now = datetime.datetime.now()
    threshold_time = now - datetime.timedelta(minutes=minutes)
    users = models.User.query.filter(models.User.created_at > threshold_time).all()

    user_dict = {}
    for user in users:
        user_dict[user.id] = {'name': user.name,
                              'age': user.age,
                              'created_at': user.created_at,
                              'updated_at': user.updated_at
                              }
    return json.dumps(user_dict, default=json_serial)


def json_serial(obj):
    if isinstance(obj, (datetime.datetime)):
        return obj.isoformat()
    raise TypeError('Type $s not serializable' % type(obj))
