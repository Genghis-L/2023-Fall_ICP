# HW3 - Ex2: Square Root

X = float(input("Enter a number: "))  # Input the number as float
Y = X / 2  # Set initial Y

while abs(X - Y**2) >= 0.001:  # Check the accuracy
    Y = (Y + X / Y) / 2

print("{:.3f}".format(Y))  # Set the output as rounding up to 3 decimals
