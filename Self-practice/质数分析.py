flag = 1
for n in range(2, 101):
    flag = 1
    print("%d" % n, end=" ")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = 0
            j = n / i
            print("= %d * %d" % (i, j), end=" ")
    if flag == 1:
        print("是一个质数")
    if flag == 0:
        print("它不是一个质数")
