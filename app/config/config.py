import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Use SQLite for local development
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    EMAIL_DOMAIN = os.getenv('EMAIL_DOMAIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Add this to suppress deprecation warning
    LOG_LEVEL = os.getenv('DEV_DATABASELOG_LEVEL_URL', 'INFO')
