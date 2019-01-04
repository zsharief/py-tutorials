# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:02:41 2018

@author: Zahid
"""

## Class attributes ##
## Instance attributes are owned by the specific instances of a class
## This means for two different instances the instance attributes are usually different
## Class attributes are owned by the class itself
## They will be shared by all the instances of the class
class A:
    a = "I am a class attribute!"
x = A()
y = A()
x.a
y.a
A.a

## modifying a class attribute
x = A()
y = A()
x.a = "This creates a new instance attribute for x!"
x.a
y.a  ## still the same
A.a
A.a = "This is changing the class attribute 'a'!"
A.a
y.a
x.a

x.__dict__
y.__dict__
A.__dict__
x.__class__.__dict__


## Examples ##
class robot:
    Three_Laws = {
            """A robot may not injure a human being or, through inaction, allow a human being to come to harm. """,
            """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
            """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
            }
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
for number, text in enumerate(robot.Three_Laws):
    print(str(number + 1) + ":\n" + text)

## count instance with class attributes
class C:
    counter = 0
    def __init__(self):
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1
if __name__ == "__main__":
    x = C()
    print("Number of instances: " + str(C.counter))
    y = C()
    print("Number of instances: " + str(C.counter))
    del x
    print("Number of instances: " + str(C.counter))
    del y
    print("Number of instances: " + str(C.counter))
if __name__ == "__main__":
    x = C()
    z = x
    print("Number of instances: " + str(C.counter))
    y = C()
    print("Number of instances: " + str(C.counter))
    del x
    print("Number of instances: " + str(C.counter))
    del y
    print("Number of instances: " + str(C.counter))
## We could have written C.counter instead of type(self).counter
## type(self) makes sense, if we use such a class as a superclass (kya farak padega??)


## Static methods ##
## Say we use private class attributes. How do we access them?
class robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances(self):
        return robot.__counter
if __name__ == "__main__":
    x = robot()
    print(x.RobotInstances())
    y = robot()
    print(y.RobotInstances())
robot.RobotInstances()
robot.RobotInstances(x)

## omitting self in RobotInstances defn
class robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances():
        return robot.__counter
robot.RobotInstances()
x = robot()
robot.RobotInstances()
x.RobotInstances()
## now we cannot call RobotInstances via an instance but can access it via the class
## The call "x.RobotInstances()" is treated as an instance method call and 
## an instance method needs a reference to the instance as the first parameter.

## We want a method, which we can call via the class name or via the instance name 
## without the necessity of passing a reference to an instance to it
## The solution consists in static methods, which don't need a reference to an instance

## Add '@staticmethod' in front of method header to make it static (decorator syntax)
class robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @staticmethod
    def RobotInstances():
        return robot.__counter
if __name__ == "__main__":
    print(robot.RobotInstances())
    x = robot()
    print(x.RobotInstances())
    y = robot()
    print(y.RobotInstances())
    print(robot.RobotInstances())


## Class methods ##
## Like static methods class methods are not bound to instances, 
## but unlike static methods class methods are bound to a class
## The first parameter of a class method is a reference to a class
## They can be called via instance or class name
class robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @classmethod
    def RobotInstances(cls):
        return cls, cls.__counter
if __name__ == "__main__":
    print(robot.RobotInstances())
    x = robot()
    print(x.RobotInstances())
    y = robot()
    print(y.RobotInstances())
    print(robot.RobotInstances())

## Use cases of class methods
## 1. factory methods
## 2. often used, where we have static methods, which have to call other static methods

## All classes in Python are derived from a special top-level parent class called Object
class fraction(object):
    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)
    @staticmethod
    def gcd(a, b):
        while b!= 0:
            a, b = b, a%b
        return a
    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
x = fraction(8,24)
print(x)

## Usefulness of class methods in inheritance
class pets:
    name = "pet animals"
    @staticmethod
    def about():
        print("This class is about {}!".format(pets.name))
class dogs(pets):
    name = "'man's best friends' (Frederick II)"
class cats(pets):
    name = "cats"
p = pets()
p.about()
d = dogs()
d.about()
c = cats()
c.about()
## Desired output for about() should have been specific to the class
## The problem is that the method 'about' does not know that it's been called by
## an instance of the dogs or cats classes
## We decorate 'about' with a classmethod decorator now
class pets:
    name = "pet animals"
    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))
class dogs(pets):
    name = "'man's best friends' (Frederick II)"
class cats(pets):
    name = "cats"
p = pets()
p.about()
d = dogs()
d.about()
c = cats()
c.about()