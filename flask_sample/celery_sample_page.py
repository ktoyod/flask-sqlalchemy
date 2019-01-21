import json
import random
from flask import Blueprint, render_template, request, redirect, url_for

from flask_sample import models
from flask_sample.database import db
from flask_sample.utils import json_serial
from flask_sample.celery import process_celery_sample

celery_sample_page = Blueprint('celery_sample_page', __name__, url_prefix='/celery_sample', template_folder='templates')


@celery_sample_page.route('/')
def index():
    return render_template('celery_sample/index.html')


@celery_sample_page.route('/process', methods=['POST'])
def process():
    id = request.form['id']
    num = int(request.form['num'])

    process_celery_sample.delay(id, num)

    return redirect(url_for('celery_sample_page.index'))


@celery_sample_page.route('/add_task', methods=['POST'])
def add_task():
    celery_task = models.CeleryTaskSample()
    celery_task.result = random.choice([0, 1, 10, 100, 1000])
    db.session.add(celery_task)
    db.session.commit()

    return redirect(url_for('celery_sample_page.index'))


@celery_sample_page.route('/results')
def result():
    all_tasks = db.session.query(models.CeleryTaskSample).all()
    all_tasks_list = []
    for task in all_tasks:
        all_tasks_list.append({
            'id': task.id,
            'result': task.result,
            'status': task.status,
            'error_message': task.error_message,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
            })
    return json.dumps(all_tasks_list, default=json_serial)
