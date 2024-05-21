# def make_dict(f):
#     d = {}
#     for i in s:
#         d.setdefault(len(i), []).append(i)
#     return d

def make_dict(f):
    d = {}
    for i in s:
        d[len(i)] = d.get(len(i), []) + [i]
    return d


f = open("mywords.txt", "r")
c = f.read()
# s = list(filter(None, c.split("\n")))
s = c.split("\n")
print(s)
print(make_dict(f))
