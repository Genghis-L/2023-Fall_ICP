p = input("Enter a chess board position: ") # Enter the position
c = ord(p[0]) + int(p[1])
# since ord(a) == 97, if c = ord(column) + int(row) is even, this case is black; otherwise, white
if c % 2 == 0:
    print("This case is black")
else:
    print("This case is white")
