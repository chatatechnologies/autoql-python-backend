# AutoQL Python Backend
## Dashboards, Query Quick Start, Data Alerts

The AutoQL Python Backend serves as a sample REST API for managing Dashboards, Query Quick Start, and Data Alerts.

Please note: This application is only intended to be an example and is missing some crucial elements, including user
authentication and error handling. Therefore, it is not recommended for Production use in its current implementation.

### Setup

This application uses Flask, Sqlite3 and Python 3.6.

To begin, create a virtual environment and install the requirements:

```pip install -r requirements.txt```

Next, define the entry point for the application:

```export FLASK_APP=app.py```

Create the database tables. This will initialize a Sqlite database called "autoql.db" in the parent directory:

```flask db upgrade```

Run the app on port 5000:

```flask run```


## Dashboards

For information on the AutoQL Dashboard frontend components, please see our Developer Documentation:

[React Dashboards](https://chata.readme.io/docs/react-dashboards)

[Vanilla JS Dashboards](https://chata.readme.io/docs/vanilla-dashboards)

### Create a Dashboard

```
POST /dashboards

Request JSON body:
{
    "project_id": "string",
    "user_id": "string",
    "name": "string",
    "data": [...]
}

* The 'data' field contains the Dashboard (an array of JSON objects) which is created in the AutoQL Dashboard widget
```
### Get Dashboards
```
GET /dashboards?project_id=project-id&user_id=user-id
```
### Update Dashboard
```
PUT /dashboards/{dashboard_id}

Request JSON Body
{
    "name": "string",
    "data": [...]
}
```

## Data Alerts

### Create Data Alert Notification via Webhook
```
POST /your-webhook

HTTP Headers:
AutoQL-Signature: <signature_token>
AutoQL-Timestamp: 1234567890000

Request JSON body:
{
    {
    "event": "data_alert.true",
    "payload": {
        "notification_id": "nt_123",
        "data_alert_id": "da_123",
        "project_id": "project1",
        "title": "High Sales",
        "message":"You've achieved your sales goal this month",
        "users": ["user1", "user2"],
        "created_at": 1605910895,
        "data_return_query": "total sales this month",
        "query_result": {
            "reference_id": "1.1.200",
            "message": "ok",
            "data":{}
            }
        }
    }
}
```
### Get Data Alert Notification
```
GET /notifications/{notification_id}
```

## Query Quick Start
Coming soon


