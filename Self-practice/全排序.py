# from itertools import permutations
#
# s = list(input())
# p = permutations(s)
# j=0
# for i in p:
#     print("".join(i))
#     j+=1
#
# print(j)

def permute(n):
    if len(n) == 1:
        return [n]
    res = []
    for i in range(len(n)):
        rest = n[:i] + n[i + 1:]
        for p in permute(rest):
            res.append([n[i]] + p)
    return res


if __name__ == "__main__":
    s = input()
    l = []
    k = 0
    for i, j in enumerate(s):
        l.append(j)
    for p in permute(l):
        print("".join(p))
        k += 1
    print(k)
