print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6  # 25 + (30/6) = 30

#100 - ((25*3)%4) = 100 - (75%4) = 100-3 = 97
#Since % calculates the remainder
print "Roosters", 100.0 - 25.0 * 3 % 4   

print "Now I will count the eggs:"

# 3 + 2 + 1 - 5 + (4%2) - (1/4) + 6 = 1 + 0 - 0 + 6 = 0.75 + 6 = 7
#Python rounds fractions down before the end of the calculation => 1/4 was instantly rounded down to 0
#Changed to floating point number so will now produce 6.75
print 3.0 + 2 + 1 - 5 + 4 % 2 - 1.0/4.0 + 6

print "Is it true that 3 + 2 < 5 - 7?"
# 3+2 < 5-7  => 5< -2 
#This is not true so False is returned
print 3.0 + 2 < 5 - 7

print "What is 3 + 2?", 3.0 + 2 #3+2 = 5
print "What is 5 - 7?", 5.0 - 7 #5-7 = -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2 #True
print "Is it greater or equal?", 5.0 >= -2 #True
print "Is it less or equal?", 5.0 <= -2 #False
