def p(n):
    s = n.split()
    a = []
    for i in s:
        a.append(i[0].upper() + '.')
    return " ".join(a)


while True:
    name = input("Please input your name: ")
    print(f'Hi! Your Name Initials are: {p(name)}')
