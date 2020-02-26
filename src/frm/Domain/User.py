# from pymongo.collation import Collation
from src.frm.Repository import UserRepository, AlertRepository, BaseRepository
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Integer, Text, Table, Float, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session

from .Alert import Alert

Base = declarative_base()


class User(Base):
    __tablename__ = 'frm_user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    frequency = Column(Integer)
    children = relationship(Alert.__tablename__)

    @property
    def alert(self):
        return self.alerts

    @alert.setter
    def alert(self, alerts):
        self.alerts = alerts
