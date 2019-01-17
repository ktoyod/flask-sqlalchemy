# flask appの初期化を行い、flask appオブジェクトの実態をもつ
from flask import Flask

from flask_sample.database import init_db
import flask_sample.models

from flask_sample.auth_page import auth_page
from flask_sample.user_page import user_page
from flask_sample.post_test_page import post_test_page
from flask_sample.hello import hello


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_sample.config.Config')

    init_db(app)

    app.register_blueprint(hello)
    app.register_blueprint(auth_page)
    app.register_blueprint(user_page)
    app.register_blueprint(post_test_page)

    return app


app = create_app()
