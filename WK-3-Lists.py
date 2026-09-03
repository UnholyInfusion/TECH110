#create an empty list
my_list = []      

# create and load an array / list with one line!
my_numbers = [ 2.1, 4.2, 6.3, 8.4 ]

# show the full list with one line
print(my_numbers)

# show me the third item - remember, starts at index 0
print( my_numbers[2] )
print( my_numbers[-1] )   # wraps around to end
print( my_numbers[-4] )

# add an item to the list
my_numbers.append(13.4) #attach to the end
my_numbers.insert(2, 33.3)  # insert at specified index
print( my_numbers )

# get input from user (or database)
num = (float(input('Enter a number: ')))
my_numbers.append(num)
my_numbers.append( float(input("Enter another number: ")) )
    
# show the full list with one line
print(my_numbers)

#pop off the last item or select an item by index
last = my_numbers.pop()
print (f'last item: {last}')
selected = my_numbers.pop(1)
print (f'Selected item: {selected}')

#remove function
my_numbers.remove(6.3)
print (my_numbers)

#find the location of an item or index an item
location = my_numbers.index(13.4)
print (f'\nlocation of 13.4: {location}')

#length of list -- how many items do we have
length = len(my_numbers)
print (f'length: {length}')

#additional list functions
largest = max(my_numbers)
smallest = min(my_numbers)
my_numbers.sort()
print (f'largest: {largest}')
print (f'smallest: {smallest}')
print (f'sorted: {my_numbers}')