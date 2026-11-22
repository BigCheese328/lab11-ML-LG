#https://github.com/BigCheese328/lab11-ML-LG.git
#Partner 1: Marcos Lima
#Partner 2: Lexie Gallagher
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b