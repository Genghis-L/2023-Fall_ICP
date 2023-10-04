# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 10 - Pattern 3 (NL)


for i in range(5):
    print("*", end="")

    for j in range(i):
        print(" *", end="")

    print()

for i in range(3, -1, -1):
    print("*", end="")

    for j in range(i):
        print(" *", end="")

    print()
