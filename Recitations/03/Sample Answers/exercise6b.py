pocket = int(input('Enter a pocket number (0-36) on a roulette wheel: '))

print()         #blank line

if x<0 or x>36:
    print('Pocket number out of range 0-36')
elif pocket==0:
    print('Pocket',pocket,'is green')
elif pocket<=10 or (pocket>18 and pocket<=28): #pocket [1-10] or [19-28]
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is black')
    else:               #odd number
        print('Pocket',pocket,'is red')
else:                                           #pocket [11-18] or [29-36]
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is red')
    else:               #odd number
        print('Pocket',pocket,'is black')

