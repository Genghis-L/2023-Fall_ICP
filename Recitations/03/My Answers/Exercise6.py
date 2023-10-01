# Roulette Wheel Colors

n = int(input("Please input a pocket number: >"))
if n not in range(0, 37):
    print("Please give a right pocket number again. ")
else:
    if n == 0:
        print("The pocket is green. ")
    elif (
        n in range(1, 11, 2)
        or n in range(12, 19, 2)
        or n in range(19, 29, 2)
        or n in range(30, 37, 2)
    ):
        print("The pocket is red. ")
    else:
        print("The pocket is black")
