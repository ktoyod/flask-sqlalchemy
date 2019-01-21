import time
from celery import Celery
from flask import Flask

from flask_sample.database import init_db, db
from flask_sample import models


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_app = Flask(__name__)
flask_app.config.from_object('flask_sample.config.DevelopmentConfig')
init_db(flask_app)
celery = make_celery(flask_app)


@celery.task
def process_celery_sample(task_id, num):
    sample_task = models.CeleryTaskSample.query.get(task_id)
    sample_task.status = 1
    db.session.commit()

    # なんらかの処理をする
    try:
        result = num * 1000 / sample_task.result
        time.sleep(30)
    except Exception as e:
        # エラーだった時
        sample_task.status = -1
        db.session.commit()
        raise ZeroDivisionError(e)

    # 処理が無事終わった時
    sample_task.result = result
    sample_task.status = 2
    db.session.commit()

    return task_id


class ZeroDivisionError(Exception):
    "ゼロ除算をしてしまった時のエラー"
