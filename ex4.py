cars = 100 #Defines the variable cars
space_in_a_car = 4.0 #Defines the variable space_in_a_car
drivers = 30 #Defines the variable drivers
passengers = 90 #Defines the variable passengers
cars_not_driven = cars - drivers #Defines the variable car_not_driven as the variable car - variable drivers = 100-30 = 70
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined

# Error on line 8 because the variable car_pool_capacity hasn't been defined/created so python cannot do the calculation. 
