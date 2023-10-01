# Software Sales

n = int(input("Please input the number of packages purchased: >"))

if n in range(0, 10):
    d = 0
    m = n * 99 * (1 - d / 100)
elif n in range(10, 20):
    d = 10
    m = n * 99 * (1 - d / 100)
elif n in range(20, 50):
    d = 20
    m = n * 99 * (1 - d / 100)
elif n in range(50, 100):
    d = 30
    m = n * 99 * (1 - d / 100)
elif n >= 100:
    d = 40
    m = n * 99 * (1 - d / 100)
else:
    print("Please input a right quantity again. ")

print(f"Discount: {d}%")
print(f"The total amount of the purchase after the discount: {m}0$")
