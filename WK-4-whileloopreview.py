answer = 'y'
count = 0

while answer == 'y':
    # code to repeat
    print('Doing the thing...')
    print(f'count: {count}')
    count += 1
    #change the condition or you will get stuck
    answer = input('Do again (y/n)? ')