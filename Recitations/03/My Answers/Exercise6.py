# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 6 - (Gaddis 3.9) - Roulette Wheel Colors

pocket_num = int(input("Please input a pocket number: >"))
if pocket_num not in range(0, 37):
    print("Please give a right pocket number again. ")
else:
    if pocket_num == 0:
        print("The pocket is green. ")
    elif (
        pocket_num in range(1, 11, 2)
        or pocket_num in range(12, 19, 2)
        or pocket_num in range(19, 29, 2)
        or pocket_num in range(30, 37, 2)
    ):
        print("The pocket is red. ")
    else:
        print("The pocket is black")
