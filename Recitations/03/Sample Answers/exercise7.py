print('Price per package: $99')
packages = int(input('How many packages you want to purchase? '))

print()             #blank line

if packages<10:
    discount = 0
elif packages<20:
    discount = 10
elif packages<50:
    discount = 20
elif packages<100:
    discount = 30
else:
    discount = 40

if discount!=0:
    print(str(discount)+'% discount')

price = packages * 99 * (1 - discount/100)
print('Total amount of purchase after discount: $' + str(price) + '0')
