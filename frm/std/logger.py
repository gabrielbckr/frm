import logging

from frm.std import Singleton


class Logger(Singleton):

    def __init__(self):
        self.log = logging.getLogger('Start Logging')
        self.log.setLevel(logging.DEBUG)
        # add console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        self.log.addHandler(console)
        super(Logger, self).__init__()
