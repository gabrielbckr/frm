from os import getenv
import yaml
from frm.std import Singleton

CONFIG_ENV = 'FRM_CONFIG'
NO_TOKEN = '__NO_TOKEN__'
NO_NAME = '__NO_NAME__'
NO_USERNAME = '__NO_USERNAME__'
NO_PASSWORD = '__NO_PASSWORD__'
LOCALHOST = 'localhost'
DB_DEFAULT = 'postgres'
DB_PORT = 5432


class Config(Singleton):

    def __init__(self):
        self.config_is_loaded = False
        self.config = yaml.safe_load(getenv(CONFIG_ENV).replace('\\n', '\n'))
        if not isinstance(self.config, dict) or not self.config:
            self.config = dict()
        else:
            self.config_is_loaded = True
        self.version = self.config.get('version', 0)
        super(Config, self).__init__()

    @property
    def is_valid(self):
        return self.config_is_loaded and len(self.config.get('databases', dict())) > 0

    @property
    def rapid7_is_valid(self) -> bool:
        return self.rapid7_token != NO_TOKEN

    @property
    def rapid7_token(self) -> str:
        return self.config.get('rapid7', dict()).get('token', NO_TOKEN)

    @property
    def rapid7_region(self):
        return self.config.get('rapid7', dict()).get('region', 'eu')

    def get_db_connection_string(self, database: str):
        databases = self.config.get('databases', dict())
        if database not in databases:
            return None
        dbconfig = databases.get(database, dict())
        db_type: str = dbconfig.get('type', DB_DEFAULT)
        user: str = dbconfig.get('user', NO_USERNAME)
        pssw: str = dbconfig.get('password', NO_PASSWORD)
        db_url: str = dbconfig.get('url', LOCALHOST)
        port: int = int(dbconfig.get('port', DB_PORT))
        db_name: str = dbconfig.get('database', NO_NAME)
        connection_string = f'{db_type}+psycopg2://{user}:{pssw}@{db_url}:{port}/{db_name}'''
        return connection_string
