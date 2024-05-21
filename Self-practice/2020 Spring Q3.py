def merge_and_sort(f1, f2):
    f3 = open("Results.txt", "w")
    c_f1 = f1.read()
    c_f2 = f2.read()
    f3.write(c_f1 + "\n" + c_f2)
    f1.close()
    f2.close()
    f3 = open("Results.txt", "r")
    c_f3 = f3.read()
    s = list(filter(None, c_f3.split("\n")))
    s.sort()
    f3 = open("Results.txt", "w")
    for i in s:
        f3.write(i + "\n")
    f3.close


f1 = open("f1.txt", "r")
f2 = open("f2.txt", "r")
merge_and_sort(f1, f2)
