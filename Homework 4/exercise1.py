# HW4 - Ex1: Word statistics

# Section 1: Getting Valid Input of Word Number
""" # A concise way to check the validity of the input
    
    while (n := int(input("How many words will you enter? > "))) not in range(3, 7):
        print("Invalid input. Please enter a number between 3 and 6")

    print(n)
    
"""

flag = (
    False  # To control the while loop, if the input is valid, then jump out of the loop
)

while flag == False:
    num_words = int(
        input("How many words will you enter? > ")
    )  # Input the number of words
    if num_words < 3 or num_words > 6:  # If the number is invalid
        print("Invalid input. Please enter a number between 3 and 6")
    else:
        flag = True  # If the number is valid


# Section 2: Inputting Words & Calculation
word = input("Word #1 please > ")  # Input the first word
L_word = word  # Set the initial longest word
S_word = word  # Set the initial shortest word
Sum_len = len(word)  # Set the initial sum of the length of words

for i in range(2, num_words + 1):  # Start inputing words from the second to the last
    word = input(f"Word #{i} please > ")
    Sum_len += len(word)  # Total sum update
    if len(word) >= len(L_word):
        L_word = word  # Update the new longest word
    if len(word) <= len(S_word):
        S_word = word  # Update the new shortest word

Ave_word = Sum_len / num_words  # Calculate the average length of words


# Section 3: Printing out Longest/Shortest Words and Average Length
print(f"Shortest: {S_word}")
print(f"Longest: {L_word}")
print(
    "Average Length: {:.2f}".format(Ave_word)
)  # Output the average length rounding up to 2 decimals
