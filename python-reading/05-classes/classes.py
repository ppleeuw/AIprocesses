"""
Project 05 — Classes, Inheritance & Dunder Methods
Difficulty 5/10

Read the design: what's inherited, what's overridden, what dunder methods enable.
"""


# --- Instance vs class attributes ----------------------------------------
class Account:
    # Class attribute: shared by ALL instances, lives on the class.
    bank = "MonoBank"

    def __init__(self, owner, balance=0):
        # Instance attributes: per-object, set in __init__.
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


a = Account("Ada")
print(a.owner)                  # predict: Ada      (from __init__)
print(a.bank)                   # predict: MonoBank  (from the class)

# Class attributes are shared — changing the class changes it for all.
Account.bank = "PolyBank"
print(a.bank)                   # predict: PolyBank


# --- Inheritance & method overriding -------------------------------------
class Animal:
    def speak(self):
        return "..."            # default: silence


class Dog(Animal):
    def speak(self):           # overrides the parent method
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


print(Dog().speak())           # predict: Woof
print(Cat().speak())           # predict: Meow


# --- super() and method resolution order (MRO) ---------------------------
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)   # call Account.__init__
        self.rate = rate

    def deposit(self, amount):
        # super() finds the NEXT method up the MRO (Account.deposit here).
        super().deposit(amount)
        # Bonus interest on deposits.
        self.balance += amount * self.rate
        return self.balance


s = SavingsAccount("Linus", 100)
s.deposit(50)
# 100 + 50 (super) + 50*0.02 = 100 + 50 + 1 = 151
print(s.balance)               # predict: 151.0


# --- Dunder methods make objects behave like built-ins -------------------
class Money:
    def __init__(self, amount):
        self.amount = amount

    # __repr__: unambiguous, developer-facing. __str__ falls back to it.
    def __repr__(self):
        return f"Money({self.amount})"

    # Defining __eq__ enables '=='. Defining __lt__ enables '<' and sorted().
    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount


wallet = [Money(30), Money(10), Money(20)]
print(wallet[0] == Money(30))  # predict: True
print(sorted(wallet))          # predict: [Money(10), Money(20), Money(30)]


# --- @property: a method that looks like an attribute --------------------
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        # Accessed as c.area (no parentheses), computed on access.
        return math.pi * self.radius ** 2


c = Circle(2)
print(c.area)                  # predict: 12.566...  (pi * 4)
