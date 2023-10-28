def proper_divisors(N):
    sum = 0                # Initialize the sum
    for i in range(1, N):
        if N % i == 0:
            sum += i       # Update the sum
    return sum


def perfect_number(N):
    if N == proper_divisors(N):
        return True
    else:
        return False


def main():
    for N in range(1, 10001):
        if perfect_number(N):
            print(N)


main()
