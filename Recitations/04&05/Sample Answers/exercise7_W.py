organisms = int(input('Starting number of organisms?\n> '))
daily_inc = input('Average daily increase (in %)?\n> ')
total_days = int(input('Number of days to multiply?\n> '))

day = 1     #sentinel variable starting day 1

if "%"in daily_inc:
    daily_inc = int(daily_inc[:-1])
else:
    daily_inc = int(daily_inc)

#header print
print('Day\tApproximate Population')

while day <= total_days:
    #print(' ' + str(day) + '\t\t ' + str(organisms))

    #better print
    print(' ' + str(day) + '\t\t ' + '%.3f' % organisms)

    organisms *= 1 + daily_inc / 100
    day += 1    #next day
