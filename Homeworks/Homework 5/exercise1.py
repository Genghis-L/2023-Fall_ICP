def greatest_common_divisor(n, m):
    for i in range(min(n, m), 0, -1):           # Reduce the time a little bit, accepting 1 as one common divisor 
        if n % i == 0 and m % i == 0:
            return i


def reduce_fraction(n, m):
    d = greatest_common_divisor(n, m)
    n, m = int(n / d), int(m / d)
    return n, m


def main():
    n = int(input("Enter the numerator: > "))   # Input the numerator
    m = int(input("Enter the denominator: > ")) # Input the denominator
    n_r, m_r = reduce_fraction(n, m)
    if n_r != n:                                # To check whether n/m can be reduced
        print(f"The fraction {n}/{m} can be reduced to {n_r}/{m_r}")
    else:
        print(f"The fraction {n}/{m} cannot be reduced")


main()
