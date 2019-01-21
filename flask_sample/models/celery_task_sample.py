from datetime import datetime

from flask_sample.database import db


class CeleryTaskSample(db.Model):
    __tablename__ = 'celery_task_sample'

    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
