# Color Mixer

c1 = input("Please input the first color: >")
c2 = input("Please input the second color: >")

if c1 not in ('red', 'blue', 'yellow') or c2 not in ('red', 'blue', 'yellow'):
    print("Please input a right color again. ")
elif (c1, c2) == ('red', 'blue') or (c2, c1) == ('red', 'blue'):
    print("The mixture is purple! ")
elif (c1, c2) == ('red', 'yellow') or (c2, c1) == ('red', 'yellow'):
    print("The mixture is orange! ")
else:
    print("The mixture is green! ")
