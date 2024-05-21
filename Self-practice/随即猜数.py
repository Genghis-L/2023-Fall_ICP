import random

n = random.randint(1, 10)
i = int(input("Please guess the number:"))
while i != n:
    i = int(input("Please guess again:"))
print("Yeah! Your guess is right! Congratulations!")
