from unittest.mock import MagicMock, patch
from app.services.user_service import UsersService

def test_create_user(app_context):
    users_service = UsersService()
    email = 'testuser@test.com'
    password = 'password123'
    hashed_password = 'hashed_password'
    user = MagicMock()
    user.email = email

    with patch('app.services.user_service.PasswordHasher.hash_password', return_value=hashed_password) as mock_hash_password, \
         patch.object(users_service.user_repository, 'create_user', return_value=user) as mock_create_user:
        result = users_service.create_user(email, password)
        assert result == user
        mock_hash_password.assert_called_once_with(password)
        mock_create_user.assert_called_once_with(email, hashed_password)

def test_login_success():
    users_service = UsersService()
    email = 'testuser@test.com'
    password = 'password123'
    hashed_password = 'hashed_password'
    user = MagicMock()
    user.user_id = 1
    user.password = hashed_password

    with patch.object(users_service.user_repository, 'get_user_by_email', return_value=user), \
        patch('app.services.user_service.PasswordHasher.check_password', return_value=True), \
        patch.object(users_service.token_service, 'create_jwt_token', return_value='test_token'):
        response_data, status_code = users_service.login(email, password)
        assert status_code == 200
        assert response_data['access_token'] == 'test_token'


def test_login_failure_wrong_password(app_context):
    users_service = UsersService()
    email = 'testuser@test.com'
    wrong_password = 'wrongpassword'
    hashed_password = 'hashed_password'
    user = MagicMock()
    user.user_id = 1
    user.password = hashed_password

    with patch.object(users_service.user_repository, 'get_user_by_email', return_value=user) as mock_get_user_by_email, \
         patch('app.services.user_service.PasswordHasher.check_password', return_value=False) as mock_check_password:
        response_data, status_code = users_service.login(email, wrong_password)
        assert status_code == 401
        assert 'Invalid credentials' in response_data['message']
        mock_get_user_by_email.assert_called_once_with(email)
        mock_check_password.assert_called_once_with(hashed_password, wrong_password)

def test_login_failure_no_user(app_context):
    users_service = UsersService()
    email = 'nonexistent@test.com'
    password = 'password123'

    with patch.object(users_service.user_repository, 'get_user_by_email', return_value=None) as mock_get_user_by_email:
        response_data, status_code = users_service.login(email, password)
        assert status_code == 401
        assert 'Invalid credentials' in response_data['message']
        mock_get_user_by_email.assert_called_once_with(email)
    