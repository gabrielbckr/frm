from frm.std import DbBase, Logger, Singleton


class DbDataSource(DbBase, Singleton):

    def __init__(self):
        Logger().log.debug('DbDataSource Initializing.')
        self._raw_connection = None
        self._session_creator = None
        super(DbDataSource, self).__init__('DB_FRM')

    def get_raw_connection(self):
        return super(DbDataSource, self).get_raw_connection()
