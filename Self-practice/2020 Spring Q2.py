def addOne(L):
    i = 1
    L[-1] += 1
    while i <= len(L):
        for j, k in enumerate(L):
            if k >= 10:
                L[j] -= 10
                if j >= 1:
                    L[j - 1] += 1
                else:
                    L.insert(0, 1)
        i += 1
    return L


print(addOne([9, 9, 9]))
