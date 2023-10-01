seconds = int(input('Enter a number of seconds: '))

print()  #blank line

if seconds<60:
    print('The number of seconds is less than one minute')
elif seconds<3600:
    minutes = seconds // 60
    seconds_left = seconds % 60
    print(seconds, 'seconds are equal to:\n',minutes,'minutes and',seconds_left,'seconds')
elif seconds<86400:
    hours = seconds // 3600
    seconds_left = seconds % 3600
    minutes = seconds_left // 60
    seconds_left = seconds_left % 60
    print(seconds, 'seconds are equal to:\n',hours,'hours,',minutes,'minutes and',seconds_left,'seconds')
else:
    days = seconds // 86400
    seconds_left = seconds % 86400
    hours = seconds_left // 3600
    seconds_left = seconds_left % 3600
    minutes = seconds_left // 60
    seconds_left = seconds_left % 60
    print(seconds, 'seconds are equal to:\n',days,'days,',hours,'hours,',minutes,'minutes and',seconds_left,'seconds')
