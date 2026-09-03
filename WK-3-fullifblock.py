age = int(input('Enter age'))
cash = float(input('Enter cash'))

if age >= 21 and cash >= 10:
    print ('Welcome to the club')
elif age >= 21:
    print('Come back when you have the cover charge.')
else:
    print('you are not old enough')