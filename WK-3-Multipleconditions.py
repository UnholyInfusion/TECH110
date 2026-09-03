# multiple conditions
temp = int( input('Enter current temperature: ') )
while temp < 72 or temp > 80:
     if temp > 80:
          print('Air conditioning is running...')
     elif temp < 72:
          print('Heater is running...')


     # change the condition or infinite loop!
     temp = int( input('Enter current temperature: ') )

print('\nDone')