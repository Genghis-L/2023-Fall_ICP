# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 4 - (Gaddis 4.6) Celsius to Farenheit Table (W)

i = 0

print("{:^10}".format("Celsius") + "{:^15}".format("Farenheit"))

while i <= 20:
    print("{:^10}".format(f"{i}°C") + "{:^15}".format(f"{i*9/5+32}°F"))
    i += 1
