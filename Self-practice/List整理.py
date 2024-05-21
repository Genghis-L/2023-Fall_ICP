while 1:
    N = input("Please input your list of numbers: ")
    ''' <Alternative>
    Numbers = filter(None, N.split(" "))
    numbers = list(map(int, Numbers))
    '''
    numbers = [int(i) for i in N.split()]
    numbers.sort()
    print(f"numbers: {numbers}")
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    even.sort()
    odd.sort()

    print(f"even = {even}", f"odd = {odd}\n", sep='\n')
