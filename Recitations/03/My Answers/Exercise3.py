# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 3 - (Gaddis 3.4) - Roman Numerals

n = int(input("Please input an integer number: "))

if n < 1 or n > 10:
    print("This is a wrong number. ")
elif n <= 3:
    print("I" * n)
elif n == 4:
    print("I" + "V")
elif n <= 8:
    print("V" + "I" * (n - 5))
elif n == 9:
    print("I" + "X")
else:
    print("X")
