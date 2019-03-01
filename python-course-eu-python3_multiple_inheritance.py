# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:30:10 2019

@author: Zahid
"""

## https://www.python-course.eu/python3_multiple_inheritance.php

## general syntax for multiple inheritance where subClassName inherits from baseClass1,...
class subClassName(baseClass1, baseClass2, baseClass3,....):
    pass

## example ##
""" 
The class Clock is used to simulate a clock.
"""
class Clock(object):
    def __init__(self, hours, minutes, seconds):
        """
        The paramaters hours, minutes and seconds have to be 
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        self.set_Clock(hours, minutes, seconds)
    def set_Clock(self, hours, minutes, seconds):
        """
        The parameters hours, minutes and seconds have to be 
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        