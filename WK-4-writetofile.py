#get input
name = input('Enter client name:')

#open the file -- 'a' to "append", 'w' to "overwrite"
output_file = open( 'clients.txt', 'a' )

#write to the file
output_file.write( name + '\n')

#close file
output_file.close()