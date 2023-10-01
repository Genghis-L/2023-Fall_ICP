Year = int(input("Year: "))
flag = 0  # A flag to check whether it is a leap year

if Year % 4 == 0:
    flag = 1
    if Year % 100 == 0:
        flag = 0
        if Year % 400 == 0:
            flag = 1

if flag == 1:
    print("Leap year")
else:
    print("Not leap year")

if Year >= 1950 and (Year - 1950) % 4 == 0:
    print("World Cup year")

if Year >= 1960 and (Year - 1960) % 4 == 0:
    print("Euro Cup year")
