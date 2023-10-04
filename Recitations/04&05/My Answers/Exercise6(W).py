# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 6 - (Gaddis 4.11) Calculating the Factorial of a Number (W)

n = int(input("Please input a nonnegative integer: >"))
i, factorial = 1, 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")
