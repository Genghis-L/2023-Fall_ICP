while True:
    Input = int(input("Check the answer:"))

    if Input == 1:
        msg = "Hello world!"
        s = msg.find(' ') + 1
        t = msg[s: -1].upper()
        print(t, t[::-1])

    if Input == 2:
        string = "Python!"
        D = {'P': 1, 'y': 2, 't': 3, \
             'h': 4, 'o': 5, 'n': 6, \
             '!': 7}
        val = 0
        for char in string:
            if D.get(char, 0) % 2 == 0:
                val = val + D.get(char, 0)
            else:
                val = val - D.get(char, 0)
        print(val)

    if Input == 3:
        a = "That is the question"
        b = a.upper()
        c = b.split()
        print(max(c))

    if Input == 4:
        try:
            m = '3.8'
            s = int(m)
            print(s)
        except:
            print('Error')

    if Input == 5:
        contents = "345"
        try:
            contents = int(contents)
        except:
            try:
                contents = float(contents)
            except:
                contents = contents
        finally:
            print(type(contents))

    if Input == 6:
        L = [2, 4, 5, 7, 6, 8, 7, 10, 12]
        for i in L:
            if i % 2 == 0:
                L.remove(i)
        print(L)

    if Input == 7:
        L1 = ["one", "two", ["three", "four"]]
        L2 = []
        for i in L1:
            L2.append(i)
        L1[2].append("five")
        print(L2)

    if Input == 8:
        L1 = ["one", "two", ["three", "four"]]
        L2 = L1[:]
        L1[2].append("five")
        L1.insert(0, "zero")
        print(L1)
        print(L2)

    if Input == 9:
        def div(x, y):
            try:
                print(x / y)
            except ZeroDivisionError:
                print("Error #1")
            except TypeError:
                print("Error #2")
            except NameError:
                print("Error #3")
            finally:
                print("Try again")


        print(div(20, 'b'))

    if Input == 10:
        my_list = ['M', 'o', 'n', 't', 'y', \
                   'P', 'y', 't', 'h', 'o', 'n']
        my_set = set()
        my_set.update(my_list)
        print(my_set)
