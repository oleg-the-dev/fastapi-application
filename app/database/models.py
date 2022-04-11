from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")

    @property
    def is_buyer(self):
        return self.role.name == 'buyer'

    @property
    def is_seller(self):
        return self.role.name == 'seller'

    def __str__(self):
        return f'{self.username}, {self.role.name}'


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.name, self.quantity}'


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    def __str__(self):
        return f'{self.name}'
