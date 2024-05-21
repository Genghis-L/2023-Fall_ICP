def hamming_distance(s1, s2):
    i = 0
    if len(s1) != len(s2):
        raise ValueError
    else:
        for j, k in enumerate(s1):
            if k != s2[j]:
                i += 1
        print(f"Hamming distance:{i}")


def main():
    s1 = input()
    s2 = input()
    # if hamming_distance(s1, s2) == ValueError:
    #     print("Lengths NOT consistent!")
    # else:
    #     print(hamming_distance(s1, s2))
    try:
        hamming_distance(s1, s2)
    except ValueError:
        print("Lengths NOT consistent!")


main()
