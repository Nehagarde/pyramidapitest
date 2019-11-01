from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    Unicode,
    Enum
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Base = declarative_base()
from .meta import Base

class Phones(Base):
    __tablename__ = 'phones'

    person_id = Column(Integer, ForeignKey('persons.id'),
                       primary_key=True)
    number = Column(Unicode(128), primary_key=True)
    location = Column(Enum('home', 'work'))

class Friends(Base):
    __tablename__ = 'friends'

    person_id = Column(Integer, ForeignKey('persons.id'),
                       primary_key=True)
    friend_of = Column(Integer, ForeignKey('persons.id'),
                       primary_key=True)
    rank = Column(Integer, default=0)

class Persons(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    surname = Column(Unicode(128), nullable=False)
    gender = Column(Enum('M', 'F'))
    age = Column(Integer)
    phones = relationship(Phones)
    friends = relationship(Friends, foreign_keys=[Friends.person_id])


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
Index('my_person_index', Persons.name,unique=True, mysql_length=255)