# Time Calculator

time = float(input("Please input your time(postive float number): >"))

day = int(time // 86400)
time -= 86400 * day
hour = int(time // 3600)
time -= 3600 * hour
minute = int(time // 60)
time -= 60 * minute
second = round(time, 2)  # Round to two decimals

print("It is ", end="")

if day > 0:
    if day == 1:
        if hour == minute == second == 0:
            print(f"{day} day. ")
        else:
            print(f"{day} day, ", end="")
    else:
        if hour == minute == second == 0:
            print(f"{day} days. ")
        else:
            print(f"{day} days, ", end="")

if hour > 0:
    if hour == 1:
        if minute == second == 0:
            print(f"{hour} hour. ")
        else:
            print(f"{hour} hour, ", end="")
    else:
        if minute == second == 0:
            print(f"{hour} hours. ")
        else:
            print(f"{hour} hours, ", end="")

if minute > 0:
    if minute == 1:
        if second == 0:
            print(f"{minute} minute. ")
        else:
            print(f"{minute} minute, ", end="")
    else:
        if second == 0:
            print(f"{minute} minutes. ")
        else:
            print(f"{minute} minutes, ", end="")

if second > 0:
    if second <= 1:
        print(f"{second} second. ")
    else:
        print(f"{second} seconds. ")
