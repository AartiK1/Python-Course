# Defines function and prints out statements using the info from the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#insert values for cheese_count and boxes_of_crackers directly into function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#pre-define variables then insert into function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese * 5, amount_of_crackers * 5)
