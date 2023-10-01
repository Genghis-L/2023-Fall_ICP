# HW4 - Ex2: Blackjack

hand = input("Enter your hand: > ")  # Input the hand
hand_value = 0  # Set the initial hand value
Ace_num = 0  # Set the initial number of Aces
i = 0  # Set the initial number for while loop

# Section 1: Interation through hand to get the hand value without Aces
for i in range(0, len(hand)):
    if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
        hand_value += 10  # Adding Face Value
        continue
    if i < len(hand) - 1:  # Promising i+1 will not be out of index range
        if hand[i] + hand[i + 1] == "10":
            hand_value += 10  # Adding '10' Pip Value
            continue  # When seeing '10' at the position '1', it is fine for the next interation to add 0 to the hand value
    if hand[i] == "A":
        Ace_num += 1  # When seeing Ace, record the Ace number, the Ace value will be calculated in the following section
        continue
    hand_value += int(hand[i])  # Adding Pip Value
    i += 1

# Section 2: Calculating Ace Value
if Ace_num > 0:
    hand_value += 1 * (
        Ace_num - 1
    )  # We can at most have one Ace to have the value 11, other Aces are all value 1
    if 11 + hand_value in range(
        17, 22
    ):  # Check the last Ace Value can be 11 or not (it is the only possible Ace to be value 11)
        hand_value += 11
    else:
        hand_value += 1

# Section 3: Giving Final Suggestion
if hand_value > 21:
    print("Bust")
elif hand_value >= 17:
    print("Stay")
else:
    print("Hit")
