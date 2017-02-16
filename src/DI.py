from inspect import signature, Parameter

from src.Exceptions.NonAnnotatedDependencyError import NonAnnotatedDependencyError

class DI:
    def __init__(self):
        pass

    def get_instance_of(self, cls):
        if "__init__" not in vars(cls):
            return cls()
        parameters = [param if not param.annotation == Parameter.empty else None for param in signature(cls.__init__).parameters.values()][1:]
        if parameters.count(None) > 0:
            raise NonAnnotatedDependencyError("Could not resolve all dependencies - Missing type annotaion")
        to_inject = [self.get_instance_of(param.annotation) for param in parameters]
        return cls(*to_inject)
