formatter = "%r %r %r %r" #defines formatter

print formatter % (1, 2, 3, 4) #prints variable formatter and inserts 1, 2, 3 & 4 into %r 
print formatter % ("one", "two", "three", "four") #same as line 3
print formatter % (True, False, False, True) #same as line 3
print formatter % (formatter, formatter, formatter, formatter) #same as line 3
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #same as line 3
