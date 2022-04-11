from pydantic import BaseModel, constr
from enum import IntEnum


class RoleEnum(IntEnum):
    buyer = 1
    seller = 2


class UserCreate(BaseModel):
    username: constr(min_length=4)
    password: constr(min_length=8)
    role_id: RoleEnum

    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'password': 'password',
                'role_id': 1,
            },
        }


class UserDB(BaseModel):
    username: str
    role_id: int

    class Config:
        orm_mode = True


class ItemTrade(BaseModel):
    quantity: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
