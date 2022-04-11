from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.models import User
from app.schemas.schemas import TokenData

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        user_id: int = payload.get('user_id')
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate(db: Session, username: str, password: str) -> User | None:
    user = db.query(User).filter_by(username=username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
