#get input
rows = int(input('How many rows? '))
for r in range(1, rows + 1):
    for c in range(1, rows +1):
        print(f'{r*c}\t', end ='')
    print()