# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 9 - (Gaddis 4.14) Pattern 2 (NL)

i = 0

while i <= 5:
    print("#", end="")

    j = 0
    while j < i:  # We shall not enter this loop when i=0
        print(" ", end="")
        j += 1

    print("#")
    i += 1
