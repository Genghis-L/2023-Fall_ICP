# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 15 - Password Generator

import random

while (length := int(input("Password size? >"))) != 0:
    for i in range(length):
        print(random.randint(0, 9), end="")

    print()
