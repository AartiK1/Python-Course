print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %r heavy." % (
    age, height, weight) #%s for height instead of %r. %r produces '5\'6"' whereas %s produces 5'6" 
    
print "What's your forname?",
forname = raw_input()
print "What's your surname?",
surname = raw_input()
print "What's your email address?",
email = raw_input()

print "So you're %r %r and your email is %r." % (
    forname, surname, email)

#raw_input:
#If the prompt argument is present, it is written to standard output without a trailing
#newline. The function then reads a line from input, converts it to a string (stripping a #trailing newline), and returns that.  
