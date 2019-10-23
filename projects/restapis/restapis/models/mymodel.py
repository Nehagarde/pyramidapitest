from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(Text)
    email = Column(Text)
    password = Column(Text)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
Index('my_user_index', Users.user_name, unique=True, mysql_length=255)