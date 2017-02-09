# PY-DI - WIP
> (name subject to change)

## What is this?

A dependency injector for python taking advantage of Python's type hints ([PEP-848](https://www.python.org/dev/peps/pep-0484/)).

## Usage

The DI class has a single static method, `get_instance_of`, which takes in the class you wish to get the instance of. This will return to you an instance of the class you pass in as an argument.

In order to declare the dependencies of your class, you simply need to annotate the `__init__` method of your class.

### Example

```python
class A:
  pass

class B:
  pass

class ToInject:
  def __init__(self, param_one: A, param_two: B):
    self.a = param_one
    self.b = param_two

# sets instance_of_class to an instance of "ToInject"  
instance_of_class = DI.get_instance_of(ToInject)
```
