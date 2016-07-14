from sys import argv #imports argv from sys module/library

script, filename = argv #defines necessary argumentsto run script

txt = open(filename) #opens the file specified 

print "Here's your file %r:" % filename #prints the filename specified
print txt.read() #reads the specified file and outputs its content

print "Type the filename again:"
file_again = raw_input("> ") #asks user to specify another filename

txt_again = open(file_again) #opens the 2nd file 

print txt_again.read() #reads the 2nd file and outputs its content
