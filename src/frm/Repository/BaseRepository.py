class BaseRepository:
    def ConvertFromModel(self, obj):
        return obj.__dict__

    def ConvertToModel(self, dict):
        modelClasss = self.meta.model()
        modelClasss .__dict__.update(dict)
        return modelClasss
