from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.db import SessionLocal, TestSessionLocal
from app.database.models import User
from app.database.utils import get_or_404
from app.core.security import verify_access_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl='auth/access-token')


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_db() -> Generator:
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth_scheme),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=settings.INVALID_CREDENTIALS,
        headers={'WWW-Authenticate': 'Bearer'},
    )
    token_data = verify_access_token(token, credentials_exception)
    user = get_or_404(
        db,
        User,
        token_data.id,
        detail=settings.USER_NOT_FOUND,
    )
    return user
