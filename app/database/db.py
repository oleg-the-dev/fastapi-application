from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Dev database
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# Test database
TEST_SQLALCHEMY_DATABASE_URL = settings.TEST_SQLALCHEMY_DATABASE_URL

test_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False,
                                autoflush=False,
                                bind=test_engine)

Base = declarative_base()
