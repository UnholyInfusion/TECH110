total_days = int(input("Enter a number of days: "))
years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30
print(f'\n{total_days}Total days')
print(f'{years}Years')
print(f'{months}Months')
print(f'{days}Days')