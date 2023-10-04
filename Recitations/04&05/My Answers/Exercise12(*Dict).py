# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 12 - Dice Statistics

import random

n = {"ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0}

for i in range(1000):
    r = random.randint(1, 6)
    if r == 1:
        n["ones"] += 1
    if r == 2:
        n["twos"] += 1
    if r == 3:
        n["threes"] += 1
    if r == 4:
        n["fours"] += 1
    if r == 5:
        n["fives"] += 1
    if r == 6:
        n["sixes"] += 1

print("After 1,000 rolls: ")

for k, v in n.items():
    print(f"we have {v} {k}")
