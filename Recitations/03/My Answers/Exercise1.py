# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 1 - (Gaddis 3.2) - Areas of Rectangles

length1 = float(input("Please input the length of the first rectangle: >"))
width1 = float(input("Please input the width of the first rectangle: >"))
length2 = float(input("Please input the length of the second rectangle: >"))
width2 = float(input("Please input the width of the second rectangle: >"))

if length1 * width1 > length2 * width2:
    print("The first rectangle has the greater area. ")
elif length1 * width1 < length2 * width2:
    print("The second rectangle has the greater area. ")
else:
    print("The two rectangles have the same area. ")
