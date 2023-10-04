# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 7 - (Gaddis 4.12) Population (W)

organisms = int(input("Starting number of organisms: >"))
daily_inc = input("Starting number of organisms: >")
day = int(input("Starting number of organisms: >"))

print("{:^5}".format("Day") + "{:^30}".format("Approximate Population"))

i = 1

while i <= day:
    print(
        "{:>4}".format(i)
        + "{:>20.3f}".format(organisms * (1 + float(daily_inc[:-1]) / 100) ** (i - 1), 3)
    )
    i += 1
