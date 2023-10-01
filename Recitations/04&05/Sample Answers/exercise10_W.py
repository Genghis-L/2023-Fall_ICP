n = 5

i = 0
while i < n-1:
    j = 0
    while j<=i:
        print('* ',end='') #no line break
        j = j+1

    print()     #line break
    i += 1


i = n
while i > 0:     #will display from n to 1 stars
    j = 0
    while j<i:
        print('* ',end='') #no line break
        j += 1

    print()     #line break
    i -= 1


