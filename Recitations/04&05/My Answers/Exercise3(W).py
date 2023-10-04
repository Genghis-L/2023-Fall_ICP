# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 3 - (Gaddis 4.4) Distance Travelled (W)

i = 1

speed = int(input("What is the speed of the vehicle in kph?: >"))
time = int(input("How many hours has it travelled? >"))

print("{:<8}".format("Hour") + "Distance Travelled")

while i <= time:
    print("{:^4}".format(i) + "{:>15}".format(speed * i))
    i += 1
