def rank(n, s):
    L = []
    for i in range(len(n)):
        L.append((s[i], n[i]))  # 同tuple把人和分数丢进去
    L.sort(reverse=True)

    d = [[]]                    # 用d是因为要把分数相等的放到一个组(list of tuples)，并且按照名字排列
    d[0].append(L[0])
    j = 0                       # j+1是group的数量
    for i in range(1, len(L)):  # 上面sort不写逆序的话这里和后面就用逆序
        if L[i][0] == d[j][0][0]:   #如果是上一组的话，丢进去；如果不是，新开一组。这里只需要考虑前面已有的最后一组是因为L已经被排序过了
            d[j].append(L[i])
        else:
            j += 1
            d.append([])
            d[j].append(L[i])

    for k in d:
        k.sort()                # 这里就把同一组的按照字母序排列了

    z = 0  
    for i in range(len(d)):
        print(f"Rank #{1+z}: {d[i][0][1]}", end="")
        for j in range(1, len(d[i])):
            print(", " + d[i][j][1], end="")
        print()
        z += len(d[i])         # z用于记rank, 一组的z一样，每组的z是前面所有组的人数和，rank是1+z

# 这里是所有的输入

rank(["Timothy", "William", "John", "Daniel"], [70, 95, 96, 70])

print("————————————————————————————")

rank(["Alice", "Bob", "Charles", "David", "Eric"], [83, 65, 83, 100, 72])

print("————————————————————————————")

rank(["x", "T", "G", "L", "P", "H", "C", "R"], [92, 56, 33, 56, 33, 74, 56, 74])
