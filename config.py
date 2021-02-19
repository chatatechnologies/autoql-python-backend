import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcdefghijklmnopqrstuvwxyz'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'autoql.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBHOOK_SECRET = 'WH_ABCDEFG'
