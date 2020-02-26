import os

from .BaseRepository import BaseRepository
from ..Util import Constants as const
from ..Domain.Alert import Alert


class AlertRepository(BaseRepository):
    class Meta:
        model = Alert
        # TODO model gets Alert class

    def __init__(self):
        self.connection_string = os.getenv(const.CONNECTION_STRING_VAR)
        pass
