# AutoQL Example Python Backend
## Dashboards, Query Prompts, Data Alerts

The AutoQL Example Python Backend serves a sample REST API for managing Dashboards, Query Prompts, and Data Alerts.

Please note that this application is only intended to be an example and is missing some crucial elements, such as user
authentication and error handling. Therefore, it is not recommended for Production use in its current implementation.

### Setup

This application uses Flask, Sqlite3 and Python 3.6.

To begin, create a virtual environment and install the requirements:

```pip install -r requirements.txt```

Next, we need to define the entry point for the application

```export FLASK_APP=app.py```

Create the database tables. This will initialize a Sqlite database called "autoql.db" in the parent directory

```flask db upgrade```

Run the app on port 5000:

```flask run```


## Dashboards

For information on the AutoQL Dashboard frontend components, please see our readme documentation:

[React Dashboards](https://chata.readme.io/docs/react-dashboards)

[Vanilla JS Dashboards](https://chata.readme.io/docs/vanilla-dashboards)

### Create a dashboard

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

## Query Prompts
Coming soon

## Data Alerts
Coming soon
