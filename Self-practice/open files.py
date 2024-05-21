import random

f = open("lotto.txt", "w")
f.write("Lucky Numbers\n")
for i in range(5):
    f.write(f"{random.randint(1, 59)}\n")
f = open("lotto.txt", "r")
c = f.read()
f.close()
s = c.split("\n")
List = []
for i in s[1:-1]:
    List.append(int(i))
print(List)
print(c.strip("\n"))
# for line in f:
#     print(line.strip("\n")
