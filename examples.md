
## Classes

general class sample:

```python
class C:
    __instances=[]
    def __init__(self,name=None):
        self.__name = str(name) if name else str(id(self))
        self.__instances.append(self.__name)
    def __del__(self):
        self.__instances.remove(self.__name)
    def numberOfInstances(self):
        return len(self.__instances)
```

pep8 formatted:

```python
class SampleClass(object):
    """
    This is a sample class with a private name.
    Has access to the names of the other instances.
    """
    __instances = []

    def __init__(self, name=None):
        self.__name = str(name) if name else str(id(self))
        self.__instances.append(self.__name)

    def __del__(self):
        self.__instances.remove(self.__name)

    def instance_number(self):
        "Get the number of instances."
        return len(self.__instances)
```

help() on a new-style class:

```
>>> help(ClassSample)
Help on class ClassSample in module __main__:

class ClassSample(__builtin__.object)
 |  This is a sample class,
 |  counts the number of instances.
 |
 |  Methods defined here:
 |
 |  __del__(self)
 |
 |  __init__(self, name=None)
 |
 |  get_instance_list(self)
 |      Return the name list of all instances (non static).
 |
 |  get_instance_number(self)
 |      Return the number of instances (non static).
 |
 |  get_name(self)
 |      Return the name of this instance.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  instances_name_list()
 |      Return the name list of all instances.
 |
 |  instances_number()
 |      Return the number of instances.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

```
>>> help(InheritedSample)
Help on class InheritedSample in module __main__:

class InheritedSample(ClassSample)
 |  Method resolution order:
 |      InheritedSample
 |      ClassSample
 |      __builtin__.object
 |
 |  Methods inherited from ClassSample:
 |
 |  __del__(self)
 |
 |  __init__(self, name=None)
 |
 |  get_instance_list(self)
 |      Return the name list of all instances (non static).
 |
 |  get_instance_number(self)
 |      Return the number of instances (non static).
 |
 |  get_name(self)
 |      Return the name of this instance.
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from ClassSample:
 |
 |  instances_name_list()
 |      Return the name list of all instances.
 |
 |  instances_number()
 |      Return the number of instances.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from ClassSample:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```


diamond inheritance problem, contructors:

```python
class First(object):
	def __init__(self):
		print "first"

class Second(object):
	def __init__(self):
		print "second"

class Third(First, Second):
	def __init__(self):
		super(Third, self).__init__()
		print "that's it"
```

multiple inheritance chain with `mro`:

```python
A = Type('A', (object,), {})
B = Type('B', (object,), {})
C = Type('C', (object,), {})
D = Type('D', (object,), {})
E = Type('E', (object,), {})
K1 = Type('K1', (A, B, C), {})
K2 = Type('K2', (D, B, E), {})
K3 = Type('K3', (D, A), {})
Z = Type('Z', (K1, K2, K3), {})

>>> Z.mro()
[Z, K1, K2, K3, D, A, B, C, E, <type 'object'>]
```


## Decorators

decorator function, keeps name and doc str:

```python
def positive_result(function):
	def wrapper(*args, **kwargs):
		result = function(*args, **kwargs)
		assert result >= 0, function.__name__ + "() result isn't >= 0"
		return result
	wrapper.__name__ = function.__name__
	wrapper.__doc__ = function.__doc__
	return wrapper

# or with functools:

def positive_result(function):
@functools.wraps(function)
	def wrapper(*args, **kwargs):
		result = function(*args, **kwargs)
		assert result >= 0, function.__name__ + "() result isn't >= 0"
		return result
	return wrapper

@positive_result
def discriminant(a, b, c):
	return (b ** 2) - (4 * a * c)
```

decorator with parameters:

```python
def bounded(minimum, maximum):
	def decorator(function):
		def wrapper(*args, **kwargs):
			result = function(*args, **kwargs)
			if result < minimum:
				return minimum
			elif result > maximum:
				return maximum
			return result
		return wrapper
	return decorator
```

easter eggs, the zen of python

```python
import this

# more fun!
dir(this)

print ''.join([(this.d[c] if c in this.d.keys() else c) for c in this.s])
```
