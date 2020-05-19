from frm.std import DbDataSource
from frm.repository import Repository
from frm.domain.friend import Friend


class FriendRepository(Repository):

    def __init__(self, db_session=None):
        if db_session is None:
            db_session = DbDataSource().get_new_connection()
        self._session = db_session
        super(FriendRepository, self).__init__(db_session, Friend)

    def create(self, friend: Friend):
        return super(FriendRepository, self).create_item(friend)

    def create_many(self, entities, return_defaults=False):
        self._session.bulk_save_objects(entities, return_defaults=return_defaults)
        self.commit()

    def delete(self, alert: Friend):
        self.delete_item(alert)

    def get_by_name(self, name: str):
        return self.db_session.query(self.obj_class).filter(Friend.name == name).all()[0]

    def get_all(self):
        return self._session.query(self.obj_class).all()

    def get_by_id(self, f_id):
        return self._session.query(self.obj_class).filter(Friend.id == f_id).all()[0]
