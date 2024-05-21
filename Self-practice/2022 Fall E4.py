def mode(L):
    p = []
    d = {}
    for i in L:
        d[i] = d.get(i, 0) + 1
    m = 1
    for j, k in d.items():
        if (k > m and m == 1) or (k == m and m > 1):
            p.append(j)
            m = k
        if k > m and m > 1:
            p = []
            p.append(j)
            m = k
    if p == []:
        return None
    elif len(p) == 1:
        return p[0]
    else:
        return p


print(mode([1, 2, 2, 3, 3, 3, 2, 1]))
print(mode(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'b']))
print(mode([1, 2, 3, 4, 5, 3, 1]))
print(mode([]))
