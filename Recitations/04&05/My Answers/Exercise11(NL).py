# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 11 - Pattern 4 (NL)

triangle = int(input("How many triangles would you like? >"))
size = int(input("What size would you like for each triangle? >"))


for i in range(triangle):
    for j in range(size):
        print("*" + " *" * j)
