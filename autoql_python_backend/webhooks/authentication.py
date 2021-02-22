import base64
import datetime
import hmac

from hashlib import sha256


WEBHOOK_TIME_WINDOW_MILLIS = 300000  # 5 minutes


def verify_webhook_signature(webhook_secret, autoql_signature_header, autoql_timestamp_header, request_body_bytes):

    signed_payload = '{}.{}'.format(autoql_timestamp_header, request_body_bytes.decode('utf-8'))
    hmac_hash = hmac.new(webhook_secret.encode('utf-8'), signed_payload.encode('utf-8'), digestmod=sha256)
    expected_signature = base64.b64encode(hmac_hash.digest()).decode()

    if expected_signature != autoql_signature_header:
        raise Exception("Signatures do not match.")

    now = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000.0)
    if (now - int(autoql_timestamp_header)) > WEBHOOK_TIME_WINDOW_MILLIS:
        raise Exception('Webhook request has expired.')
