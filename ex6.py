#inserts 10 in place of %d. %d means a digit. Defines variable x
x = "There are %d types of people." % 10
binary = "binary" #defines variable binary
do_not = "don't" #defines variable do_not
#Defines variable y. %s means string. 1st %s inserts binary and 2nd %s inserts do_not 
y = "Those who know %s and those who %s." % (binary, do_not)

#prints x and y
print x 
print y

print "I said: %r." % x #inserts variable x in place of %r
print "I also said: '%s'." % y #inserts variable y instead of %s

hilarious = False #Defines variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r" #Defines variable joke_evaluation and inserts a to be determined string in place of %r

print joke_evaluation % hilarious #inserts hilarous in place of %r in the variable joke_evaluation

#defines variables w and e
w = "This is the left side of..."
e = "a string with a right side."

#combines the 2 strings w and e to create 1 longer string
print w + e

#Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
