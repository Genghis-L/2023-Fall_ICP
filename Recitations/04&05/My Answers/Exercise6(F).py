# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 6 - (Gaddis 4.11) Calculating the Factorial of a Number (F)

n = int(input("Please input a nonnegative integer: >"))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
