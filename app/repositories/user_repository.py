from sqlalchemy import and_
from app.config.config import Config
from app.utils.decorators import with_session
from app.models.user import User


class UserRepository:
    

    @with_session
    def get_user_by_email(self, email, session=None):
        return session.query(User).filter(
            and_(User.email == str(email), User.is_deleted.is_(False))
        ).first()

    @with_session
    def create_user(self, email, password, session=None):
        user_exists = session.query(User).filter_by(email=email).first()
        if user_exists:
            return f"User with email {email} already exists"
        user = User(email=email, password=password)  # Password should be hashed
        session.add(user)
        session.commit()
        return user

    @with_session
    def seed_admin_user(self, email, password, session=None):
        admin_exists = session.query(User).filter_by(email=email).first()
        if not admin_exists:
            return self.create_user(email, password)
