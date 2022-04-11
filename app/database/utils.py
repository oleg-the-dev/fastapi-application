from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.db import Base


def get_or_404(
        db: Session,
        model: Base,
        instance_id: int,
        detail: str = settings.INSTANCE_NOT_FOUND,
) -> Base:
    '''
    Get instance from database, if no instance was found raise 404 error.
    '''
    instance = db.query(model).get(instance_id)
    if not instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )
    return instance
