import datetime

print('Enter the first date:')
year1 = int(input('Year:'))
month1 = int(input('Month:'))
day1 = int(input('Day:'))

print('')

print('Enter the second date:')
year2 = int(input('Year:'))
month2 = int(input('Month:'))
day2 = int(input('Day:'))


date_1 = datetime.date(year1, month1, day1)
date_2 = datetime.date(year2, month2, day2)

diff = date_2 - date_1

if diff.days == 1:
    print('The difference between your two dates is', diff.days, 'day')
elif diff.days > 1:
    print('The difference between your two dates is', diff.days, 'days')
else:
    print('There is no difference between your dates')
