import time

seconds = int( input('Enter seconds: ') )

for count in range(seconds, 0, -1):
    print(f'seconds remaining: {count}')
    time.sleep(1)

print('Happy New Year!')