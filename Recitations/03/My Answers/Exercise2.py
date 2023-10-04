# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 2 - (Gaddis 3.3) - Age Classiﬁer

age = int(input("Please input a person's age: >"))

if age <= 1:
    print("This person is an infant. ")
elif age < 13:
    print("This person is a child. ")
elif age < 20:
    print("This person is a teenager. ")
else:
    print("This person is an adult. ")
