def longest_repetition(L):
    d = {}
    for j in L:
        d[j] = 1
    if L == []:
        return None
    else:
        for i in range(1, len(L)):
            if L[i] == L[i - 1] and d[L[i]] == 1:
                d[L[i]] += 1
            if L[i] == L[i - 1] and d[L[i]] > 1:
                m = 1
                for j in L[i:]:
                    if j == L[i]:
                        m += 1
                    else:
                        break
                d[L[i]] = max(d[L[i]], m)
        s = list(d.values())
        s.sort()
        for j, k in d.items():
            if k == s[-1]:
                return j


print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
print(longest_repetition([1, 2, 3, 4, 5]))
print(longest_repetition([]))
