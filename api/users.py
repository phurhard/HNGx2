#!/usr/bin/env python3
'''User model'''
# import required linraries
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class User(Base):
    '''The user model'''
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        '''Initialization'''
        self.id = str(uuid.uuid4())
        self.name = name

    def save(self, session):
        '''Saves the current session to the database'''
        session.add(self)
        session.commit()

    @classmethod
    def all(cls, session):
        '''Gets all the users'''
        return session.query(cls).all()

    @classmethod
    def get(cls, session, user_id):
        '''Gets a user instamce from the database'''
        return session.query(cls).filter_by(id=user_id).first()

    def to_json(self):
        '''Serialization of the user class'''
        return {'id': self.id, 'name': self.name}

    def delete(self, session):
        '''Removes the instamce feom the db'''
        session.delete(self)
        session.commit()

