total_nb_bugs = 0
day_nb = 0

while day_nb < 5:
    day_nb += 1
    nb_bugs = int(input('How many bug for day {0}?\n> '.format(day_nb)))
    total_nb_bugs += nb_bugs

print('Total number of bugs: {0}'.format(total_nb_bugs))
