# HW3 - Ex1: Checking user input

flag = (
    False  # To control the while loop, if the input is valid, then jump out of the loop
)

while flag == False:
    score = int(input("Score: "))  # Input the score
    if score < 0 or score > 100:  # If the score is invalid
        print("Invalid input. Please enter a score between 0 and 100.")
    else:
        flag = True  # If the score is valid

if score >= 95:  # Do not need to set the upper bound since the input is already valid
    print("Your grade is A")
elif score >= 90:
    print("Your grade is A-")
elif score >= 87:
    print("Your grade is B+")
elif score >= 83:
    print("Your grade is B")
elif score >= 80:
    print("Your grade is B-")
elif score >= 77:
    print("Your grade is C+")
elif score >= 73:
    print("Your grade is C")
elif score >= 70:
    print("Your grade is C-")
elif score >= 67:
    print("Your grade is D+")
elif score >= 63:
    print("Your grade is D")
else:  # Do not need to set the lower bound since the input is already valid
    print("Your grade is F")
