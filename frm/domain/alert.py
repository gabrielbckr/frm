from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Column, DateTime, Boolean
from frm.domain import Base
from frm.domain.friend import Friend


class Alert(Base):
    __tablename__ = 'frm_alert'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer, ForeignKey(Friend.id))
    trigger_time = Column(DateTime, nullable=False)
    solve_time = Column(DateTime)
    is_solved = Column(Boolean, default=False, nullable=False)

    def __str__(self) -> str:
        return f'<{self.id}>'

    def __repr__(self):
        return self.__str__()
