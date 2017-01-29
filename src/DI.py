class DI:
    def __init__(self):
        pass

    @staticmethod
    def get_instance_of(cls):
        if "__init__" not in vars(cls):
            return cls()
        annotations = cls.__init__.__annotations__  # type: dict
        to_inject = [DI.get_instance_of(annotation) for annotation in annotations.values()]
        return cls(*to_inject)