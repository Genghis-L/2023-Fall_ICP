N = int(input('Enter a strictly positive integer: '))

x, y = 0, 1

print(x)

i = 1

while i <= N:
    print(y)
    x,y = y, (x+y)
    i = i + 1

