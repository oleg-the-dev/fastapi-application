from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.models import User
from app.core.dependencies import get_db
from app.core.security import get_password_hash
from app.schemas.schemas import UserCreate, UserDB

router = APIRouter(
    tags=['Users'],
    prefix='/users'
)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UserDB)
def create_user(
        user: UserCreate,
        db: Session = Depends(get_db),
) -> User:
    user_exists = db.query(User).filter_by(username=user.username).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=settings.INVALID_USERNAME,
        )
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        password=hashed_password,
        role_id=user.role_id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
