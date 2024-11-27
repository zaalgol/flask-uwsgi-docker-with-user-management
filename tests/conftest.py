# tests/conftest.py

import pytest
from app.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'
    app.config['JWT_SECRET_KEY'] = 'test_jwt_secret_key'
    app.config['ADMIN_PASSWORD'] = 'test_admin_password'
    app.config['EMAIL_DOMAIN'] = 'test.com'
    app.config['LOG_LEVEL'] = 'CRITICAL'  # Suppress logging during tests
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def app_context(app):
    with app.app_context():
        yield
