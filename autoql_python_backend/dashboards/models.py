import datetime as dt

from autoql_python_backend import db


class Dashboard(db.Model):

    __tablename__ = 'dashboards'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(512), nullable=False)
    user_id = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    data = db.Column(db.JSON, nullable=False, default={})
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    def __init__(self, project_id, user_id, name, data):
        self.project_id = project_id
        self.user_id = user_id
        self.name = name
        self.data = data

    def __repr__(self):
        return '<Dashboard {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "user_id": self.user_id,
            "name": self.name,
            "data": self.data,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }
