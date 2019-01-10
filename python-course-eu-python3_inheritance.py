# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:50:15 2019

@author: Zahid
"""

## https://www.python-course.eu/python3_inheritance.php

## python supports inheritance, and multiple inheritance
## superclass, ancestor; subclass, heir, or child class

## Syntax and Simple Inheritance Example ##
# class DerivedClassName(BaseClassName):
#     pass

class person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last    
    def name(self):
        return self.firstname + " " + self.lastname    
class employee(person):
    def __init__(self, first, last, staffnum):
        person.__init__(self, first, last)
        self.staffnumber = staffnum
    def get_employee(self):
        return self.name() + ", " + self.staffnumber
x = person("Marge", "Simpson")
y = employee("Homer", "Simpson", "1007")
print(x.name())
print(y.get_employee())
## The __init__ method of employee class explicitly invokes the __init__ method of the
## person class. We can also use super().__init__()
# def __init__(self, first, last, staffnum):
#     super().__init__(first, last) ## why no 'self' in argument??
#     # or
#     # super(employee, self).__init__(first, last)
#     self.staffnumber = staffnum


## Overloading and overriding ##
## put the functionality of 'name' into the __str__ method
class person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def __str__(self):
        return self.firstname + " " + self.lastname
class employee(person):
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum
x = person("Marge", "Simpson")
y = employee("Homer", "Simpson", "1007")
print(x)
print(y)
## If we print an instance of the employee class, the __str__ mthod of person is used
## This is due to inheritance
## put the functionality of 'get_employee' into the str method
## overriding the __str__ method from person in employee
class person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)
class employee(person):
    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum
    def __str__(self):
        return super().__str__() + ", " + self.staffnumber
x = person("Marge", "Simpson", 36)
y = employee("Homer", "Simpson", 28, "1007")
print(x)
print(y)
## Method overriding is an object-oriented programming feature that allows a subclass
## to provide a different implementation of a method that is already defined by
## its superclass or by one of its superclasses
## The implementation in the subclass overrides the implementation of the superclass
## by providing a method with the same name, same parameters or signature, and 
## same return type as the method of the parent class

## Overloading is the ability to define the same method, with the same name but with
## a different number of arguments and types. It is the ability of a function to 
## perform different tasks, depending on the number of parameters or the types of params

## example of same number of params but with different types
def successor(number):
    return number + 1
successor(1)
successor(1.6)
## Function works for both integer and float values

## Overloading functions with different no of params doesn't work in python
def f(n):
    return n + 42
def f(n, m):
    return n + m + 42
f(3,4)
f(3)
## Overriding means that the first definition isn't available anymore
## This form of overloading can be simulated with default params
def f(n, m = None):
    if m:
        return n + m + 42
    else:
        return n + 42
## The '*' operator is a more general way for a family of fns with 1,2,3, or more params
def f(*x):
    if len(x) == 1:
        return x[0] + 42
    else:
        return x[0] + x[1] + 42