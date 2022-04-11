from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    SECRET_KEY: str = 'secret'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    SQLALCHEMY_DATABASE_URL: str = f'sqlite:///{BASE_DIR}/dev.db'

    # Errors
    USER_NOT_FOUND: str = 'User not found'
    ITEM_NOT_FOUND: str = 'Item not found'
    INSTANCE_NOT_FOUND: str = 'Instance not found'
    INVALID_CREDENTIALS: str = 'Invalid credentials'
    INVALID_USERNAME = 'Invalid username. Try another'

    # Test
    TEST_SQLALCHEMY_DATABASE_URL: str = f'sqlite:///{BASE_DIR}/test.db'
    TEST_USER_USERNAME = 'testuser'
    TEST_USER_PASSWORD = 'password'
    TEST_USER_ROLE_ID = 1

    class Config:
        case_sensitive = True


settings = Settings()
