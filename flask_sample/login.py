from flask_login import LoginManager

from flask_sample import models

login_manager = LoginManager()


def init_login(app):
    login_manager.login_view = '/auth/login'
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)
