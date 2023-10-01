minutes = 10    #sentinel variable (we start from 10 minutes)

#repeat code for the given minutes until we exceed 30 minutes
while minutes <= 30:
    calories = 4.2 * minutes
    print(minutes,'minutes:\t',calories,'calories burned')
    minutes +=5
