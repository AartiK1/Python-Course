from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." #exits script
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#open(filename, mode)
#modes:
    # r --> read only
    # w --> write only (an existing file with the same name will be erased)
    # a --> opens the file for appending; any data written to the file is automatically added to the end
    # r+ --> opens the file for both reading and writing
    # if mode argument is omitted, mode 'r' is assumed
target = open(filename, 'w')

# Following not necessary as the file is opened in write only mode!
# print "Truncating the file.  Goodbye!"
# target.truncate() 

print "Now I'm going to ask you for three lines."

#user defines the variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#write('x') writes "x" to the file
#(line1, line2, line3) is a sequence of string elements
# .join() returns a string in which the elements of sequence have been joined by str seperator
# in this case, '\n' is the string seperator

target.write('\n'.join((line1, line2, line3)) + '\n' ) 



print "And finally, we close it."
target.close() #closes the file
