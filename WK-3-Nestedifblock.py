age = int(input('Enter age: '))

if age >= 21:
    cash = float(input('Enter cash: '))
    if cash >= 10:
        print ('welcome to the club')
    else:
        print ('come back when you have the cover charge')
else:
    print('you are too young to enter.')