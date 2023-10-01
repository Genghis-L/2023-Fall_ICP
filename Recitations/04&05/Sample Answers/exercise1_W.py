days = 0        #sentinel variable to keep track of the number of days
total_bugs = 0  #total number of bugs

#repeat until we have entered bugs for 5 days
while days != 5:
    bugs = int(input('How many bugs today?\n> '))
    total_bugs += bugs   #add to the total
    days +=1        #increment the sentinel variable to move to next day

#out of the loop: meaning we have collected bugs for 5 days
print()     #blank line
print('Total Number of Bugs:', total_bugs)
