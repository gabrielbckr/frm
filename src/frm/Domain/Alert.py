from datetime import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Integer, Text, Table, Float, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .User import User

Base = declarative_base()


class Alert(Base):

    __tablename__ = 'frm_alert'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.__tablename__+'.id'))
    trigger_time = Column(DateTime)

    def solve(self, time=None):
        if time:
            self.solveTime(time)
        else:
            self.solveTime(datetime.now)

    @property
    def is_solved(self):
        return self.solveTime > datetime.now()
