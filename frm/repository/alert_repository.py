from frm.repository import Repository
from frm.std import DbDataSource
from frm.domain import Alert
from datetime import datetime


class AlertRepository(Repository):

    def __init__(self, db_session=None):
        if db_session is None:
            db_session = DbDataSource().get_new_connection()
        self._session = db_session
        super(AlertRepository, self).__init__(db_session, Alert)

    def create(self, alert: Alert):
        return super(AlertRepository, self).create_item(alert)

    def create_many(self, entities, return_defaults=False):
        self._session.bulk_save_objects(entities, return_defaults=return_defaults)
        self.commit()

    def get_by_active(self):
        return self.db_session.query(self.obj_class) \
            .filter(Alert.is_solved == False) \
            .all()

    def delete(self, alert: Alert):
        self.delete_item(alert)

    def get_by_trigger_time_grater(self, date: datetime):
        return self.db_session.query(self.obj_class) \
            .filter(Alert.trigger_time >= date).all()

    def get_top_by_user_id(self, user_id):
        return self._session.query(self.obj_class) \
            .fitler(Alert.user_id == user_id) \
            .order_by(Alert.trigger_time.desc()) \
            .limit(1)
