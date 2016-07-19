from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)  --> opens file and stores it as variable in_file
#indata = in_file.read()    --> reads in_file and stores it as indata
indata = open(from_file).read() #simplifies the top 2 lines and means you don't need to close in_file as shown in the last line

#gets the length of the string that you pass through it and returns a number
print "The input file is %d bytes long" % len(indata) 

#if to_file:
    #already exists, returns True
    #doesn't exist, returns False
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input() #allows user to exit script if they don't want to overwrite an exisiting file

# opens to_file as write only and saves it as out_file
out_file = open(to_file, 'w')
# writes the data from the from_file to to_file
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()
