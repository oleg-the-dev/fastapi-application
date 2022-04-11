from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.models import Item, User
from app.database.utils import get_or_404
from app.core.dependencies import get_db, get_current_user
from app.schemas.schemas import ItemTrade

router = APIRouter(
    prefix='/items',
    tags=['Items'],
)


@router.post('/{item_id}/buy')
def buy_items(
        item_id: int,
        trade: ItemTrade,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
) -> Item:
    item = get_or_404(
        db,
        Item,
        item_id,
        detail=settings.ITEM_NOT_FOUND,
    )
    if current_user.is_seller:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )
    if not item.quantity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    if item.quantity < trade.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    item.quantity -= trade.quantity
    db.commit()
    db.refresh(item)
    return item


@router.post('/{item_id}/sell')
def sell_items(
        item_id: int,
        trade: ItemTrade,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user),
) -> Item:
    item = get_or_404(
        db,
        Item,
        item_id,
        detail=settings.ITEM_NOT_FOUND,
    )
    if current_user.is_buyer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )
    item.quantity += trade.quantity
    db.commit()
    db.refresh(item)
    return item
