# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 13 - FizzBuzz

for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    else:
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        print()
