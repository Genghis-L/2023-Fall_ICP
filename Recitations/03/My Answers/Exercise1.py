# Area of Rectangles
l1 = float(input("Please input the length of the first rectangle: >"))
w1 = float(input("Please input the width of the first rectangle: >"))
l2 = float(input("Please input the length of the second rectangle: >"))
w2 = float(input("Please input the width of the second rectangle: >"))

if l1 * w1 > l2 * w2:
    print("The first rectangle has the greater area. ")
elif l1 * w1 < l2 * w2:
    print("The second rectangle has the greater area. ")
else:
    print("The two rectangles have the same area. ")
