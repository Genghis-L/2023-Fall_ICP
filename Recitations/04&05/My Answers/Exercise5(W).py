# Copyright 2023 Genghis, 骆可瀚, kl4747@nyu.edu

# Exercise 5 - (Gaddis 4.10) Tuition Increase (W)

tuition = 8000
i = 1

while i <= 5:
    print("{:^13}".format(f"Year {i}") + "{:>32}".format(f"Projected Tuition"))
    print(f"First Semester" + "{:>26}".format(f"${round(tuition,2)}"))
    print(f"Second Semester" + "{:>25}".format(f"${round(tuition,2)}"))
    tuition *= 1.03
    i += 1
