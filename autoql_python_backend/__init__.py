from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from autoql_python_backend.dashboards import routes, models
from autoql_python_backend.data_alerts import routes, models
from autoql_python_backend.webhooks import routes
