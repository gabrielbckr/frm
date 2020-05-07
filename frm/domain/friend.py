from sqlalchemy import Integer, Text, Column
from frm.domain import Base


class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)#, nullable=False, autoincrement=True)
    name = Column(Text)
    frequency = Column(Integer)

    def __str__(self) -> str:
        return f'<Friend(name="{self.name}>'

    def __repr__(self):
        return self.__str__()
