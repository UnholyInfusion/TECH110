age = int(input('Enter age: '))
cash = float(input('Enter cash: '))

if age >= 16:
    print('You are old enough to drive!')
else:
    print('You are to young to drive!')

if age >= 21 and cash >= 10:
    print('Welcome to the club')
else:
    print('You must be 21 and must have the cover charge')

if age >= 21 or cash >= 1000000:
    print('Welcome to the club')
else:
    print('You must be 21 or have $1000000')