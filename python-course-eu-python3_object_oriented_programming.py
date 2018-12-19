# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:35:48 2018

@author: Zahid
"""

class robot:  ## header of class
    pass  ## body of class

if __name__ == "__main__":
    x = robot()
    y = robot()
    y2 = y
    print(y2 == y)
    print(x == y)


## Attributes ##
## Attributes are created inside of a class definition
## We can dynamically create arbitrary new attributes for existing instances of a class. 
## We do this by joining an arbitrary name to the instance name, separated by a dot "."
class robot:
    pass
x = robot()
y = robot()

x.name = "Marvin"
x.build_year = "1979"

y.name = "Caliban"
y.build_year = "1993"

print(x.name)
print(y.build_year)

## Above is not the right way to create instance attributes
## Each instance possesses a dictionary __dict__ which stores its attributes and corresp values
x.__dict__
y.__dict__

## Attributes can be bound to class names
class robot():
    pass
x = robot()
robot.brand = "Kuka"
x.brand
x.brand = "Thales"
x.brand
robot.brand
y = robot()
y.brand
robot.brand = "Thales"
y.brand
x.__dict__
y.__dict__
robot.__dict__

## If you try to access y.brand, Python checks first, if "brand" is a key of the 
## y.__dict__ dictionary. If it is not, Python checks, if "brand" is a key of the
## Robot.__dict__. If so, the value can be retrieved.
## An attribute error is raised if an attribute is not present in either of the two dicts
x.energy
## This error may be avoided with the getattr() method by specifying a default
getattr(x, 'energy', 100)

## We can bind an attribute to a function name as well
def f(x):
    return 42
f.x = 50
print(f(10))
print(f.x)
## This can be used as a replacement for static function variables in C/C++ in python
def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    return "Monty Python"
for i in range(10):
    print(f(i))
print(f.counter)


## Methods ##
def hi(obj):
    print("Hi, I am " + obj.name + "!")

class robot:
    pass

x = robot()
x.name = "Marvin"
hi(x)

## bind func to a class attribute
class robot:
    say_hi = hi ## 'say_hi' is the method here
x = robot()
x.name = "Marvin"
robot.say_hi(x)
x.say_hi()
## following method calls are equivalent
type(x).say_hi(x)
robot.say_hi(x)
x.say_hi()
## need for __init__ initializer
y = robot()
y.say_hi()


## The __init__ method ##

class A:
    def __init__(self):
        print("__init__ has been executed!")
x = A()

class robot:
    def __init__(self, name = None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
x = robot()
x.say_hi()
y = robot("Marvin")
y.say_hi()


## Data abstraction ##
class robot:
    def __init__(self, name = None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

x = robot()
x.set_name("Henry")
x.say_hi()
y = robot()
y.set_name(x.get_name())
print(y.get_name())

## adding additional attribute 'build_year' with getter and setter methods
class robot:
    def __init__(self, name = None, build_year = None):
        self.name = name
        self.build_year = build_year
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It is not known, when I was created!")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_build_year(self, build_year):
        self.build_year = build_year
    def get_build_year(self):
        return self.build_year
x = robot("Henry", 2008)
y = robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()

## __str__ and __repr__ methods ##
## These are both 'magic methods'
## We can depict various data as strings using the str function, which uses the internal
## __str__ method of the corresponding data type. 
## __repr__ also produces a string representation
l = ["Python", "Java", "C++", "Perl"]
print(l)
str(l)
repr(l)

d = {"a":3497, "b":8011, "c":8300}
print(d)
str(d)
repr(d)

x = 587.78
str(x)
repr(x)

## If you apply str or repr to an object, Python is looking for a corresponding 
## method __str__ or __repr__ in the class definition of the object.
class A:
    pass
a = A()
print(a)
str(a)
repr(a)
a
## As both methods are unavailable, Python uses the default output for object "a"

class A:
    def __str__(self):
        return "42"
a = A()
print(repr(a))
print(str(a))
print(a)
a

class A:
    def __repr__(self):
        return "42"
a = A()
print(repr(a))
eval(repr(a))
print(str(a))
str(a)
print(a)
a

## choice between __str__ and __repr__
## use __str__ if output is for the end user, that is, if it should be nicely printed
## use __repr__ for the internal representation of an object
l = [3,8,9]
s = repr(l)
s
l == eval(s)
l == eval(str(l))
## eval() can only be applied on the strings created by repr
import datetime
today = datetime.datetime.now()
str_s = str(today)
eval(str_s)
repr_s = repr(today)
t = eval(repr_s)
type(t)
## eval(repr_s) returns again a datetime.datetime object
## The String created by str can't be turned into a datetime.datetime object by parsing.

class robot:
    def __init__(self, name = None, build_year = None):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "robot('" + self.name + "'," + str(self.build_year) + ")"
if __name__ == "__main__":
    x = robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type  of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new: ", type(new))
## When __str__ is not defined but __repr__ is, str(object) method returns the same 
## output as repr().
## Extending with an __str__ method
class robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"
    def __str__(self):
        return "Name: " + self.name + ", Build_year: " + str(self.build_year)
if __name__ == "__main__":
    x = robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new: ", type(new))
## gives an error as eval cannot convert x_str back to a robot object
if __name__ == "__main__":
    x = robot("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new: ", type(new))


## Public, Protected and Private attributes ##
class A:
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
x = A()
x.pub
x.pub = x.pub + " and my value can be changed"
x.pub
x._prot
x.__priv

## Data Encapsulation means, that we should only be able to access private 
## attributes via getters and setters
## Defining build_year and name as private attributes
class robot():
    def __init__(self, name = None, build_year = 2000):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_build_year(self, build_year):
        self.__build_year = build_year
    def get_build_year(self):
        return self.__build_year
    def __repr__(self):
        return "'robot('" + self.__name + "', " + str(self.__build_year) + ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build_year: " + str(self.__build_year)
if __name__ == "__main__":
    x = robot("Marvin", 1979)
    y = robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
        
## General template for class with priv attr with getters and setters
class A():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def GetX(self):
        return self.__x
    def SetX(self, x):
        self.__x = x
    def GetY(self):
        return self.__y
    def SetY(self, y):
        self.__y = y
## There are at least two good reasons against such an approach
  
      
## Destructors ##
## It is called when the del statement is called? Similar to str()
class robot:
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print("Robot has been destroyed!")
if __name__ == "__main__":
    x = robot("Tik-Tok")
    y = robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
if __name__ == "__main__":
    x = robot("Tik-Tok")
    y = robot("Jenkins")
    # z = x
    print("Deleting x")
    del x
    # print("Deleting z")
    # del z
    del y

## personalizing the __del__ method gives an error
## reason to be discussed later
class robot:
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print(self.name + " says bye-bye!")
if __name__ == "__main__":
    x = robot("Tik-Tok")
    y = robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
    
    
## https://www.python-course.eu/python3_object_oriented_programming.php