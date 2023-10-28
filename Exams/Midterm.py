print("Q1 (5 points)")

# x = "Alomomola"
# i = 1
# while i < len(x) + 1:
#     print(x[-i], end="")
#     i += 1

print()

print("Q2 (5 points)")

# a = 0
# b = 1
# while a < 1:
#     b, a = a, b
# print(a)

print()

print("Q3 (5 points)")

# total = 0
# answer = "yeah"
# while answer != "yeah" or answer != "yes":
#     print("give me five!")
#     answer = "yes"
# print("Done!")

print()

print("Q4 (5 points)")

# n = 6
# for i in range(n):
#     print("#", end="")
#     for j in range(i):
#         print(" ", end="")
#     print("#")

print()

print("Q5 (10 points)")

# m = 6
# n = 3
# i = 1
# while i < m:
#     j = 1
#     while j <= i and i <= n:
#         print("*", end="|")
#         j += 1
#     j += 1
#     while j <= m and i > n:
#         print("*", end="|")
#         j += 1
#     print()
#     i += 1

print()

print("Q6 (10 points)")

# answer = input("Type something plz: ")
# while answer != "yes" and answer != "yeah":
#     print("I'm in yr while loop")
#     answer = input("Type something plz: ")

print()

print("Q7 (10 points)")

# answer = input("Type something plz: ")
# another = input("Type another plz: ")

# if answer == "no" and another == "n":
#     print("Ohhh no!")
# elif answer == "yes" or another == "y":
#     print("Yeaaahhhh")
# else:
#     print("Huh?")

print()

print("Q8 (20 points)")
# Solution 1

# n = int(input("Please enter a number > "))
# s = 1

# while s < 3:
#     n_pre = n
#     n = int(input("Please enter a number > "))
#     if n == n_pre:
#         s += 1
#     else:
#         s = 1

# print("Done!")

# Solution 2
# n = int(input("Please enter a number > "))
# n_pre1 = n - 1
# n_pre2 = n - 2

# while not (n == n_pre1 and n_pre1 == n_pre2):
#     n_pre2 = n_pre1
#     n_pre1 = n
#     n = int(input("Please enter a number > "))

# print("Done!")

print()

print("Q9  (15 points)")

# n = int(input("Please input an integer: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i**j, end=" ")
#     print()

# print()

print("Q10 (15 points)")

# n = int(input("Please enter the number of strings > "))

# s = ""
# for i in range(n):
#     s_new = input("Please enter the number of strings > ")
#     s = s + s_new

# m_num = 0
# n_num = 0
# for i in s:
#     if i == "m":
#         m_num += 1
#     if i == "n":
#         n_num += 1

# print(f"Number of ms: {m_num} ; Number of ns: {n_num}")

print()
