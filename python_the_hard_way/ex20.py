from sys import argv

script, input_file = argv

#prints the whole doc
def print_all(f):
    print f.read()

#goes back to the start of the file
def rewind(f):
    f.seek(0)

#prints a line
def print_a_line(line_count, f):
    print line_count, f.readline()

#specify which file you want to open
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 #=1
print_a_line(current_line, current_file)

current_line += 1 #=2
print_a_line(current_line, current_file)

current_line += 1 #3
print_a_line(current_line, current_file)


