# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 7 - (Gaddis 3.12) - Software Sales

package_num = int(input("Please input the number of packages purchased: >"))

if package_num in range(0, 10):
    discount = 0
    money = package_num * 99 * (1 - discount / 100)
elif package_num in range(10, 20):
    discount = 10
    money = package_num * 99 * (1 - discount / 100)
elif package_num in range(20, 50):
    discount = 20
    money = package_num * 99 * (1 - discount / 100)
elif package_num in range(50, 100):
    discount = 30
    money = package_num * 99 * (1 - discount / 100)
elif package_num >= 100:
    discount = 40
    money = package_num * 99 * (1 - discount / 100)
else:
    print("Please input a right quantity again. ")

print(f"Discount: {discount}%")
print(f"The total amount of the purchase after the discount: {money}0$")
