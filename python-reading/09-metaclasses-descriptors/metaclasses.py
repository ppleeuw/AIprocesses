"""
Project 09 — Metaclasses & Descriptors
Difficulty 9/10

Descriptors intercept attribute access; metaclasses customize class creation.
"""


# --- A descriptor: intercepts instance attribute access ------------------
# Defined as a CLASS attribute, but it manages per-instance storage.
class Validated:
    def __init__(self, min_value=0):
        self.min_value = min_value

    # __set_name__ is called automatically when the descriptor is assigned
    # to a class attribute; tells us the attribute name to use for storage.
    def __set_name__(self, owner, name):
        self.name = name          # e.g. "age"

    # __get__ runs on 'instance.attr' access.
    def __get__(self, instance, owner):
        if instance is None:      # accessed on the class (Person.age)
            return self
        return instance.__dict__.get(self.name, self.min_value)

    # __set__ runs on 'instance.attr = value'. This is what makes it a
    # DATA descriptor (beats the instance __dict__).
    def __set__(self, instance, value):
        if value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        instance.__dict__[self.name] = value


class Person:
    age = Validated(min_value=0)   # descriptor as a class attribute

    def __init__(self, age):
        # Triggers Validated.__set__ -> validation runs here.
        self.age = age


p = Person(30)
print(p.age)                    # predict: 30   (via __get__)


# --- __init_subclass__: the modern hook for subclass creation ------------
# Runs when a subclass is DEFINED (not instantiated). Cleaner than a metaclass
# for most "register / validate subclasses" needs.
class Plugin:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls.__name__)
        print(f"registered {cls.__name__}")


# Defining Dog triggers __init_subclass__ NOW (at class definition time).
class Dog(Plugin):
    pass


print(Plugin.registry)          # predict: ['Dog']


# --- A minimal metaclass: type.__new__ -----------------------------------
# A metaclass's instances are classes. type is the default metaclass.
# Overriding __new__ lets us customize class creation.
class LoggedMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"creating class {name}")   # runs at 'class' definition time
        return super().__new__(mcs, name, bases, namespace)


# "creating class Config" prints when THIS line executes, not at instantiation.
class Config(metaclass=LoggedMeta):
    pass


c = Config()                    # no extra print — instance creation is unaffected


# --- Recap: how 'property' is just a descriptor --------------------------
# @property builds a data descriptor with __get__/__set__ under the hood.
class Temperature:
    def __init__(self, celsius):
        self._c = celsius

    @property
    def fahrenheit(self):
        return self._c * 9 / 5 + 32


t = Temperature(0)
print(t.fahrenheit)            # predict: 32.0  (accessed like an attribute)
