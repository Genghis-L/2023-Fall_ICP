def print_value():
    value = 'Local or Global?'
    print(value)


value = 'I am global'
print_value()
print(value)


def access_to_global():
    global a
    a += 1


a = 1
print(a)
access_to_global()
print(a)
