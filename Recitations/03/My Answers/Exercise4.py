# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 4 - (Gaddis 3.7) - Color Mixer

color1 = input("Please input the first color: >")
color2 = input("Please input the second color: >")

if color1 not in ('red', 'blue', 'yellow') or color2 not in ('red', 'blue', 'yellow'):
    print("Please input a right color again. ")
elif (color1, color2) == ('red', 'blue') or (color2, color1) == ('red', 'blue'):
    print("The mixture is purple! ")
elif (color1, color2) == ('red', 'yellow') or (color2, color1) == ('red', 'yellow'):
    print("The mixture is orange! ")
else:
    print("The mixture is green! ")
