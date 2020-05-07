from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .friend import Friend
from .alert import Alert
