from app.services.hassing_service import PasswordHasher

def test_hash_and_check_password():
    password = 'password123'
    hashed_password = PasswordHasher.hash_password(password)
    assert password != hashed_password
    assert PasswordHasher.check_password(hashed_password, password) is True
    assert PasswordHasher.check_password(hashed_password, 'wrongpassword') is False