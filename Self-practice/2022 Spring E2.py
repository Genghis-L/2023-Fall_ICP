size = 4
for i in range(1, size + 1):
    print(' ' * size, end='')  # single space
    for j in range(size - i):
        print(' ', end='')  # single space
    for j in range(i):
        print('* ', end='')  # star and space
    print()
for i in range(1, size + 1):
    for j in range(size - i):
        print(' ', end='')  # single space
    for j in range(i):
        print('* ', end='')  # star and space
    for j in range(size - i):
        print(' ', end='')  # double space
    for j in range(i):
        print('* ', end='')  # star and space
    print()
