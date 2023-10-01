n = 6

i = 0

while i < n: #will represent number of spaces

    print('#',end='')  #no line break

    j = 0
    while j < i: #repeat for the number of spaces
        print(' ',end='')  #no line break
        j += 1

    print('#')          #with line break

    i = i+1

