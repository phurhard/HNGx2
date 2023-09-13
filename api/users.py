#!/usr/bin/env python3
'''User model'''
# import required linraries
from datetime import datetime
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
    created = Column(String)
    
    def __init__(self, name):
        '''Initialization'''
        self.id = str(uuid.uuid4())
        self.name = name
        self.created = str(datetime.utcnow())

    def save(self, session):
        '''Saves the current session to the database'''
        session.add(self)
        session.commit()

    @classmethod
    def all(cls, session):
        '''Gets all the users'''
        return session.query(cls).all()

    @classmethod
    def get(cls, session, user_name):
        '''Gets a user instamce from the database'''
        return session.query(cls).filter_by(name=user_name).first()

    def to_json(self):
        '''Serialization of the user class'''
        return {'id': self.id, 'name': self.name, 'created': self.created}

    def delete(self, session):
        '''Removes the instamce feom the db'''
        session.delete(self)
        session.commit()

