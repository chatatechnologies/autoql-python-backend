from flask import jsonify

from autoql_python_backend import app
from .models import DataAlertNotification


@app.route('/notifications/<string:notification_id>')
def get_notification_data(notification_id):

    notification = DataAlertNotification.query.filter_by(notification_id=notification_id).first()
    return jsonify(notification.to_dict()), 200
