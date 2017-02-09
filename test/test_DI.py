from unittest import TestCase

from src.DI import DI
from src.Exceptions.NonAnnotatedDependencyError import NonAnnotatedDependencyError


class ClassWithNoDependencies:
    pass


class ClassWithSingleDependency:
    def __init__(self, a: ClassWithNoDependencies):
        self.a = a


class ClassWithTwoDependencies:
    def __init__(self, a: ClassWithNoDependencies, b: ClassWithNoDependencies):
        self.a = a
        self.b = b


class ClassWithNonAnnotatedDependency:
    def __init__(self, a):
        self.a = a


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

    def test_given_class_with_non_annotated_dependency_when_getting_instance_throw_exception(self):
        self.assertRaises(NonAnnotatedDependencyError, DI.get_instance_of, ClassWithNonAnnotatedDependency)
