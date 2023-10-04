# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 5 - (Gaddis 3.8) - Hot Dog Cookout Calculator
# 1 hotdog = 1 hotdog (sausage) + 1 hot dog bun (bread)

people = int(input("Please input the number of people attending the cookout: >"))
hotdog_person = int(
    input("Please input the number of hot dogs each person will be given: >")
)

hotdog_total = hotdog_person * people

if hotdog_total % 10 > 0:
    hotdog_package = hotdog_total // 10 + 1
else:
    hotdog_package = hotdog_total // 10
hotdog_left = 10 * hotdog_package - hotdog_total

if hotdog_total % 8 > 0:
    hotdogbun_package = hotdog_total // 8 + 1
else:
    hotdogbun_package = hotdog_total // 8
hotdogbun_left = 8 * hotdogbun_package - hotdog_total

print("The minimum number of packages of hot dogs required:", hotdog_package)
print("The minimum number of packages of hot dog buns required:", hotdogbun_package)

print("The number of hot dogs that will be left over:", hotdog_left)
print("The number of hot dog buns that will be left over:", hotdogbun_left)
