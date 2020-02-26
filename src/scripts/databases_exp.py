# from pymongo.collation import Collation
from src.frm.Repository import UserRepository, AlertRepository, BaseRepository
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Integer, Text, Table, Float, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'frm_user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    frequency = Column(Integer)


class Alert(Base):
    __tablename__ ='frm-alert'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('frm_user.id'))
    trigger_time = Column(DateTime)