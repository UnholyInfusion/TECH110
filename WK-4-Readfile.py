input_file = open( 'clients.txt', 'r' )

for line in input_file:
    name = line [:-1]
    print (name)

input_file.close()