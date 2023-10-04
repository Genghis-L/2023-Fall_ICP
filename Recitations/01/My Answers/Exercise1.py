# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 1 - Evaluate expression

import math

"""
    Priority of the Operations: 
        0. '()' Parentheses
        1. '**' Exponentiation
        2. '+,-' Unary + or - (Sign)
        3. '*,/,//,%' Multiplication, Division, Integer Division, Modulo
        4. '+,-' Addition and Substraction
"""

# Special Examples
print(0.1 + 0.2)
print(round(0.1 + 0.2, 1))
print()

print(0.3 - 0.2)
print(round(0.3 - 0.2, 1))
print()

print(0.1 * 0.2)
print(round(0.1 * 0.2, 2))
print()

print(2 / 1)  # Always float (or complex)
print()

print(-4.5 // 2, 4 // 2)  # The lower integer in float
print(int(-2.01),int(2.99)) 
'''
    1. int() generates only integer; '//' generates float/integer based on the number type
    2. int(a) rounds down when a is positive, rounds up when a is negative; '//' only rounds down
'''
print()

print(-1.12 % 2)  # A positive float
print(-1.12 - 2 * (-1.12 // 2))
print(round(-1.12 % 2, 2))
"""
    a % b = a - b * (a // b)
"""
print()

print(-1.1 ** math.sqrt(2))  # Exponentiation has the higher priority than sign
print()
