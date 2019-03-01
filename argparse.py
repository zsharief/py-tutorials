# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 00:25:08 2019

@author: Zahid
"""

## ArgumentParser ##
from argparse import ArgumentParser

## positional arguments
parser = ArgumentParser(description = "for help and reference")
parser.add_argument("num1", type = int, help = "first number")
parser.add_argument("num2", type = int, help = "second number")
args = parser.parse_args()
print args.num1 * (args.num2**2)
# python script.py 2 4
# 32
# python script.py 4 2
# 16
## arguments are positional
# python script.py -h  ## for help

## optional arguments
# parser.add_argument("-<shorthand notation>", "--<longhand notation>", help = "<help>")
parser = ArgumentParser(description = "for help and reference")
parser.add_argument("-n1", "--num1", type = int, help = "first number")
parser.add_argument("-n2", "--num2", type = int, help = "second number")
args = parser.parse_args()
print args.num1 * (args.num2**2)
print args.n1 * (args.n2**2)  ## gives error; shorthand only meant to be used in command line, not inside program
# python script.py -n1 2 -n2 4
# 16
# python script.py -n2 4 -n1 2
# 16
# python script.py -h

parser = ArgumentParser(description = "for help and reference")
parser.add_argument("-n1", "--num1", type = int, metavar = "", help = "first number")  ## to unclutter help
parser.add_argument("-n2", "--num2", type = int, metavar = "", help = "second number")  ## to unclutter help
args = parser.parse_args()
print args.num1 * (args.num2**2)

## if optional argument not specified, the program assumes it to be None
## to make optional argument compulsory use required option in add_argument()
parser = ArgumentParser(description = "for help and reference")
parser.add_argument("-n1", "--num1", type = int, required = True, help = "first number")
parser.add_argument("-n2", "--num2", type = int, required = True, help = "second number")
args = parser.parse_args()
print args.num1 * (args.num2**2)

## mutually exclusive arguments
parser = ArgumentParser(description = "for help and reference")
parser.add_argument("-n1", "--num1", type = int, required = True, help = "first number")
parser.add_argument("-n2", "--num2", type = int, required = True, help = "second number")
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action = "store_true", help = "print quiet")
group.add_argument("-v", "--verbose", action = "store_true", help = "print verbose")
## action = "store_true" makes the default value of argument false and makes it true if the argument/flag is called
args = parser.parse_args()
