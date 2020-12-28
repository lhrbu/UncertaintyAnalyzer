class JsonSerializerHook:
    @classmethod
    def FromDict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj