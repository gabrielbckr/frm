from .BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    class Meta:
        model = []
        # TODO model gets UserClass

    def __init__(self):
        pass

    def get_user_by_name(self, name):
        pass

    def upsert_user(self, user):
        pass
