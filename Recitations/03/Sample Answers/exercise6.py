pocket = int(input('Enter a pocket number (0-36) on a roulette wheel: '))

print()         #blank line

if x<0 or x>36:
    print('Pocket number out of range 0-36')
elif pocket==0:
    print('Pocket',pocket,'is green')
elif pocket<=10:
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is black')
    else:               #odd number
        print('Pocket',pocket,'is red')
elif pocket<=18:
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is red')
    else:               #odd number
        print('Pocket',pocket,'is black')
elif pocket<=28:
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is black')
    else:               #odd number
        print('Pocket',pocket,'is red')
else:
    if pocket%2==0:     #even number
        print('Pocket',pocket,'is red')
    else:               #odd number
        print('Pocket',pocket,'is black')

    
