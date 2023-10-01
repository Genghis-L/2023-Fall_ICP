nb_cal_per_min = 4.2

minutes = 10

print('Minutes\t\tCalories')
print('--------------------')
while minutes <= 30:
    print(minutes,'\t\t',int(nb_cal_per_min * minutes))
    minutes += 5
