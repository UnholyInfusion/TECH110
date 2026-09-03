# get input
item_price = float( input("Enter price: ") )
quantity = int( input("Enter quantity: ") )

# process input
total = item_price * quantity

# show output
print(f"Total: ${total:.2f}")