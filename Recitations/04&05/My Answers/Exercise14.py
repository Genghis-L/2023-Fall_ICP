# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 14 - Fibonacci

N = int(input("Please input a stictly positive integer value: >"))

n_pre_pre, n_pre = 0, 1

print(n_pre_pre) # Because N is strictly positive

for i in range(N):
    n_pre_pre, n_pre = n_pre, n_pre_pre + n_pre
    print(n_pre_pre)
