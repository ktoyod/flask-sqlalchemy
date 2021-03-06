# flask appの初期化を行い、flask appオブジェクトの実態をもつ
from flask import Flask

from flask_sample.database import init_db
from flask_sample.login import init_login

from flask_sample.auth_page import auth_page
from flask_sample.user_page import user_page
from flask_sample.post_test_page import post_test_page
from flask_sample.hello import hello
from flask_sample.sqlalchemy_test import sqlalchemy_test
from flask_sample.celery_sample_page import celery_sample_page


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kohei toyoda dayo'
    app.config.from_object('flask_sample.config.Config')

    init_db(app)
    init_login(app)

    app.register_blueprint(hello)
    app.register_blueprint(auth_page)
    app.register_blueprint(user_page)
    app.register_blueprint(post_test_page)
    app.register_blueprint(sqlalchemy_test)
    app.register_blueprint(celery_sample_page)

    return app


app = create_app()
