def get_averages(t):
    f = open(t, "r")
    d = {}
    while True:
        c = f.readline().strip("\n")
        if c == "":
            break
        elif "grade1" in c:
            continue
        L, sum = [], 0
        L = c.split(",")
        name = L[0] + " " + L[1]
        L[0] = name
        for i in L[2:]:
            sum += int(i)
        average = int(sum / (len(L) - 1))
        d[L[0]] = average
    f.close()
    return d


print(get_averages("student_grade.csv"))
