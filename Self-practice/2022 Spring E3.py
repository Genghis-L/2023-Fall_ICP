def my_sort(L):
    for k in range(len(L) - 1):
        i = 0
        j = 1
        while j <= len(L) - 1 - k:
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
            i += 1
            j += 1
    return L


my_list = [3, 2, 4, 1, 5]
print(my_sort(my_list))
