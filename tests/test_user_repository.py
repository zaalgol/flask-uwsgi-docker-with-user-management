from unittest.mock import MagicMock
from app.repositories.user_repository import UserRepository
from app.models.user import User

def test_create_user():
    user_repository = UserRepository()
    email = 'testuser@test.com'
    password = 'password123'

    # Mock the session
    mock_session = MagicMock()
    # Mock query to return None (user does not exist)
    mock_session.query.return_value.filter_by.return_value.first.return_value = None

    # Inject mock_session into the method
    result = user_repository.create_user(email, password, session=mock_session)
    assert isinstance(result, User)
    assert result.email == email
    # Ensure that add and commit were called
    mock_session.add.assert_called_once_with(result)
    mock_session.commit.assert_called_once()

def test_create_existing_user():
    user_repository = UserRepository()
    email = 'testuser@test.com'
    password = 'password123'
    existing_user = User(email=email, password=password)

    # Mock the session
    mock_session = MagicMock()
    # Mock query to return an existing user
    mock_session.query.return_value.filter_by.return_value.first.return_value = existing_user

    # Inject mock_session into the method
    result = user_repository.create_user(email, password, session=mock_session)
    assert isinstance(result, str)
    assert 'already exists' in result
    # Ensure that add and commit were not called
    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()

def test_get_user_by_email():
    user_repository = UserRepository()
    email = 'testuser@test.com'
    existing_user = User(email=email, password='password123')

    # Mock the session
    mock_session = MagicMock()
    # Mock query to return an existing user
    mock_session.query.return_value.filter.return_value.first.return_value = existing_user

    # Inject mock_session into the method
    result = user_repository.get_user_by_email(email, session=mock_session)
    assert result == existing_user
