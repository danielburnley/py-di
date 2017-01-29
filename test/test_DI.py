from unittest import TestCase

from src.DI import DI


class ClassWithNoDependencies:
    pass


class ClassWithSingleDependency:
    def __init__(self, a: ClassWithNoDependencies):
        self.a = a


class ClassWithTwoDependencies:
    def __init__(self, a: ClassWithNoDependencies, b: ClassWithNoDependencies):
        self.a = a
        self.b = b


class ClassWithSingleDependencyWithDependency:
    def __init__(self, a: ClassWithSingleDependency):
        self.a = a


class TestDI(TestCase):
    def test_given_class_with_no_dependencies_when_getting_instance_return_class_correctly(self):
        self.assertIsInstance(DI.get_instance_of(ClassWithNoDependencies), ClassWithNoDependencies)

    def test_given_class_with_single_dependency_when_getting_instance_instantiate_class_correctly(self):
        cls = DI.get_instance_of(ClassWithSingleDependency)
        self.assertIsInstance(cls, ClassWithSingleDependency)
        self.assertIsInstance(cls.a, ClassWithNoDependencies)

    def test_given_class_with_multiple_dependencies_when_getting_instance_instantiate_class_correctly(self):
        cls = DI.get_instance_of(ClassWithTwoDependencies)
        self.assertIsInstance(cls, ClassWithTwoDependencies)
        self.assertIsInstance(cls.a, ClassWithNoDependencies)
        self.assertIsInstance(cls.b, ClassWithNoDependencies)

    def test_given_class_which_depends_on_class_with_dependency_when_getting_instance_instantiate_class_correctly(self):
        cls = DI.get_instance_of(ClassWithSingleDependencyWithDependency)
        self.assertIsInstance(cls, ClassWithSingleDependencyWithDependency)
        self.assertIsInstance(cls.a, ClassWithSingleDependency)
        self.assertIsInstance(cls.a.a, ClassWithNoDependencies)
