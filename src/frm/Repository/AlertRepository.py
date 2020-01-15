from .BaseRepository import BaseRepository
import os
from ..Util import Constants  as const

class AlertRepository(BaseRepository):
    class Meta:
        model = []
        # TODO model gets Alert class

    def __init__(self):
        self.connection_string = os.getenv(const.CONNECTION_STRING_VAR)
        pass