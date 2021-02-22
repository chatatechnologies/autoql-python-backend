import datetime
from autoql_python_backend import db


class DataAlertNotification(db.Model):

    __tablename__ = 'data_alert_notifications'

    notification_id = db.Column(db.String(64), primary_key=True)
    data_alert_id = db.Column(db.String(64), nullable=False)
    event = db.Column(db.String(256), nullable=False)
    project_id = db.Column(db.String(256), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    message = db.Column(db.String(1024), nullable=False)
    data_return_query = db.Column(db.String(), nullable=False)
    query_result = db.Column(db.JSON(), nullable=False)
    users = db.Column(db.JSON(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, event, payload):
        self.notification_id = payload['notification_id']
        self.data_alert_id = payload['data_alert_id']
        self.event = event
        self.project_id = payload['project_id']
        self.title = payload['title']
        self.message = payload['message']
        self.data_return_query = payload['data_return_query']
        self.query_result = payload['query_result']
        self.users = payload['users']
        self.created_at = datetime.datetime.utcfromtimestamp(payload['created_at'])

    def __repr__(self):
        return '<Notification {}>'.format(self.notification_id)

    def to_dict(self):
        return {
            'notification_id': self.notification_id,
            'data_alert_id': self.data_alert_id,
            'data_return_query': self.data_return_query,
            'title': self.title,
            'message': self.message,
            'query_result': self.query_result
        }
