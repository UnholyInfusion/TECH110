# counting and accumulation
deposits = [ ]          # create an empty list 
single = 0.0

while True:             # infinite loop 
     single = float( input('Enter deposit (-1 to stop): ') )
     if single < 0.0:
         break          # break out of the infinite loop
     else:
          deposits.append(single)
else:
     print('This does not run since break was used')


# statistics 
total = sum(deposits)
count = len(deposits)
average = total / count
print(f"\nTotal Deposited: ${total:,.2f}")
print(f"Number Deposits: {count}")
print(f"Average Deposit: ${average:,.2f}")
print(f"Minimum Deposit: ${min(deposits):,.2f}")
print(f"Maximum Deposit: ${max(deposits):,.2f}")
