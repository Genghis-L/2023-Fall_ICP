phase = input("Is the moon full? If yes enter Full if no enter No: ")
distance = int(input("Enter the distance of the moon from the earth: "))
date = int(input("Enter the date of the month: "))
eclipse = bool(input("Is there an eclipse? Enter True for yes and False for no: "))

flag = 0  # A flag to check whether it is special or not

if phase == "No":
    print("Moon")
else:
    if distance < 230000: # To check whether it is Super
        print("Super", end=" ")
        flag = 1
    if date == 29 or 30 or 31: # To check whether it is Blue
        print("Blue", end=" ")
        flag = 1
    if eclipse == True:  # To check whether it is Blood
        print("Blood", end=" ")
        flag = 1
    if flag == 1:
        print("Moon")
    else: # falg==0 means it is not special
        print("Full Moon")
