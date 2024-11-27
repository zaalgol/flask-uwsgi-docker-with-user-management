import logging
from app.config.config import Config
from app.services.user_service import UsersService


class InitialDataService:
    def __init__(self):
        self.users_service = UsersService()
        self.logger = logging.getLogger(__name__)

    def seed_admin_user(self):
        email = f'admin@{Config.EMAIL_DOMAIN}'
        password = Config.ADMIN_PASSWORD
        result = self.users_service.create_user(email, password)
        if isinstance(result, str):
            self.logger.info(result)
        else:
            self.logger.info(f'Admin user {email} created successfully.')
