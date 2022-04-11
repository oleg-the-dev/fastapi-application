from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.dependencies import get_db
from app.core.security import authenticate, create_token
from app.schemas.schemas import Token

router = APIRouter(
    tags=['Authentication']
)


@router.post('/auth/access-token', response_model=Token)
def auth_access_token(
        user_credentials: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
) -> dict:
    user = authenticate(
        db,
        user_credentials.username,
        user_credentials.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=settings.INVALID_CREDENTIALS,
        )
    access_token = create_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'bearer'}
