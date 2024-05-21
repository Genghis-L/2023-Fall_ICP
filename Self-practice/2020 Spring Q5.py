def sticky_wal(n):
    l = []
    l.append("")
    for i in range(1, n + 1):
        l.append("")
        for j in range(i):
            l[i] += chr(ord('a') + j)
        print("a" + '{:>{width}}'.format(l[i], width=n))
    return True


sticky_wal(int(input()))
