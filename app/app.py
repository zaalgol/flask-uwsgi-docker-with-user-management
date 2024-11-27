from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from app.config.config import Config
from app.config.logger import configure_logging


db = SQLAlchemy() # its's global to allow import the 'db' object from app

def init_admin_user(app):
    from app.services.initial_data_service import InitialDataService # to avoid circular dependencies
    with app.app_context():
        initial_data_service = InitialDataService()
        initial_data_service.seed_admin_user()


def create_app():
    jwt = JWTManager()
    migrate = Migrate()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Apply CORS to the entire app with support for credentials
    CORS(app, supports_credentials=True)

    from app.routes.api import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configure logging
    configure_logging(app)

    init_admin_user(app)

    return app
