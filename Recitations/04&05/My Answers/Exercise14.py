# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 14 - Fibonacci



N = int(input("Please input a stictly positive integer value: >"))

n_pre_pre, n_pre = 0, 1

print(n_pre_pre) # Because N is strictly positive

for i in range(N):
    n_pre_pre, n_pre = n_pre, n_pre_pre + n_pre
    print(n_pre_pre)


# def fib(n):
#     if n<0: 
#         print("It is a WRONG number") 
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(int(input("Please input a number: >"))))
