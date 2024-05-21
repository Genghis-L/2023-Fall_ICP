def get_words(t):
    d = {}
    f = open(t, "r")
    c = f.read()
    s = c.strip("\n").split("\n")
    for i in s:
        d[i] = len(i)
    f.close()
    return d


def find_anagrams(w, d):
    L = []
    for j, k in d.items():
        p = 0
        if k == len(w):
            for z in w:
                if z in j:
                    p = 1
                else:
                    p = 0
                    break
        if p == 1:
            L.append(j)
    return L


def main():
    st = input("Enter a word:\n")
    L = find_anagrams(st, get_words(input("Enter the text file:\n")))
    R = ", ".join(L)
    if R == "":
        print(f"The word {st} has no anagram")
    else:
        print(f"The anagrams of {st} are: {R}")


if __name__ == "__main__":
    main()
