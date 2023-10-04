# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 1 - (Gaddis 4.1) Bug Collector (W)

sum, i = 0, 0

while i < 5:
    sum += int(input(f"Please input the amount of bugs collected for day {i+1}: >"))
    i += 1

print(f"The total number of bugs collected in 5 days is: {sum}")
