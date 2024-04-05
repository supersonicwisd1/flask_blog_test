import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """
    Base configuration class. Contains default configuration settings + shared settings.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'insecurekeyfordev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(days=90)

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SERVER_NAME = 'localhost:8000'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskblog:blogpassword@localhost/flaskblog'

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    SERVER_NAME = 'localhost:5000' 
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"  # Use in-memory SQLite database for tests