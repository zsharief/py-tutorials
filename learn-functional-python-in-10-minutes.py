# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:34:51 2018

@author: Zahid
"""

## In an imperative paradigm, you get things done by giving the computer 
## a sequence of tasks and then it executes them 
## While executing them, it can change states/variables

## In a functional paradigm, you don’t tell the computer what to do but
## rather you tell it what stuff is
## Because of this, variables cannot vary
## Because of this, functions have no side effects in the functional paradigm
## A 'side effect' is where the function changes something outside of it

a = 3
def some_func():
    global a
    a = 5
some_func()
print(a)
## In the functional paradigm, functions can only calculate something and return it

## If a function is called twice with the same parameters, it’s guaranteed to 
## return the same result. This is called 'referential transparency'

## Typically, in functional programming, recursion is used instead of loops
def factorial_recursive(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    else:
        return n * factorial_recursive(n - 1)

## Some programming languages are also 'lazy'
## This means that they don’t compute or do anything until the very last second


## Map ##
