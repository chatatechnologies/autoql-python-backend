from flask import current_app, jsonify, request

from autoql_python_backend import app, db
from autoql_python_backend.data_alerts.models import DataAlertNotification

from .authentication import verify_webhook_signature


@app.route('/your-webhook', methods=['POST'])
def webhook():

    webhook_secret = current_app.config.get('WEBHOOK_SECRET')

    try:
        verify_webhook_signature(
            webhook_secret,
            request.headers.get('AutoQL-Signature'),
            request.headers.get('AutoQL-Timestamp'),
            request.data
        )

    except Exception as ex:
        return jsonify({'error': str(ex)}), 401

    json_data = request.get_json()

    # Only data alert events are supported at this time
    if 'data_alert' in json_data['event']:
        notification = DataAlertNotification(json_data['event'], json_data['payload'])
        db.session.add(notification)
        db.session.commit()

    return jsonify({'message': 'ok'}), 200
