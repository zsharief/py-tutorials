# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:04:25 2019

@author: Zahid
"""
## https://www.python-course.eu/python3_properties.php


## properties
## getters and setters; also known as mutator methods
## Data encapsulation: bundling of data with the methods that operate on it
class p:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
p1 = p(42)
p2 = p(4711)
p1.get_x()
p1.set_x(47)
p1.set_x(p1.get_x() + p2.get_x())
p1.get_x()

## no getters and setters
class p:
    def __init__(self, x):
        self.x = x
p1 = p(42)
p2 = p(4711)
p1.x
p1.x = 47
p1.x = p1.x + p2.x
p1.x

## Suppose if a value larger than 1000 is assigned, x should be set to 1000
class p:
    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = p(1001)
p1.get_x()
p2 = p(15)
p2.get_x()
p3 = p(-1)
p3.get_x()
## Let's assume we have designed our class with the public attribute and no methods
## People have already used it a lot and they have written code like this:
## p1 = P(42)
## p1.x = 1001
## Our new class means breaking the interface. The attribute x is not available anymore
## This is why in some languages private attributes are used with getters and setters
## Python solves this problem with 'properties'
class p:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = p(1001)
p1.x
p1.x = -12
p1.x
## A method which is used for getting a value is decorated with "@property"
## The method which has to function as the setter is decorated with "@x.setter"
## If the function had been called "f", we would have to decorate it with "@f.setter"
## we wrote "two" methods with the same name and a different number of 
## parameters "def x(self)" and "def x(self,x)".
## This is not possible, but it works due to the decorating

## Alternative way to define a property
class p:
    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(get_x, set_x)
p1 = p(1001)
p1.x
p1.x = -12
p1.x
p1.set_x = 10
## But now we have two ways to access or change the value of x
## p1.x = 42, or, p1.set_x(42)
## Using private getter and setter methods solves that
class p:
    def __init__(self, x):
        self.__set_x(x)
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)
p1 = p(100)
p1.x
p1.__set_x(12)
p1.x = 12
p1.x

## Following example has internal attributes which can't be accessed from outside
## It also shows that a property can be deduced from more than one attribute
class robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp
    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable"
        elif s <= 0:
            return "I feel bad"
        elif s <= 0.5:
            return "Could be worse"
        elif s <= 1:
            return "Seems to be okay"
        else:
            return "Great"
x = robot("Marvin", 1979, 0.2, 0.4)
y = robot("Caliban", 1993, -0.4, 0.3)
print(x.condition)
print(y.condition)


## Public instead of private attributes
## Assume a class "OurClass" which has a public attribute "OurAtt"
class OurClass:
    def __init__(self, a):
        self.OurAtt = a
x = OurClass(10)
print(x.OurAtt)
## Now suppose we have to ensure that "OurAtt" ahs a value between 0 and 1000
## without changing the interface for the end user
class OurClass:
    def __init__(self, a):
        self.OurAtt = a
    @property
    def OurAtt(self):
        return self.__OurAtt
    # @f.setter
    # def f(self, a): ## does not work
    @OurAtt.setter
    def OurAtt(self, a):
        if a < 0:
            self.__OurAtt = 0
        elif a > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = a
x = OurClass(12)
print(x.OurAtt)

## For the users of a class, properties are syntactically identical to ordinary attr's