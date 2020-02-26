class BaseRepository:

    def ConvertFromModel(self, obj):
        return obj.__dict__

    @staticmethod
    def ConvertToModel(self, original_dict):
        modelClasss = self.meta.model()
        modelClasss .__dict__.update(original_dict)
        return modelClasss
