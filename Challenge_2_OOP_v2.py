# main.py
from Challenge_2_OOP import Vehicle

# Create two instances of the Vehicle class
car1 = Vehicle("Car1", 4, 120, 0)
bike = Vehicle("Bike", 1, 80, 0)

# Call methods on the instances
print("Initial mileage of Car1:", car1._mileage)
car1.travel(50)
print("Mileage after traveling 50 units with Car1:", car1._mileage)

print("\nInitial mileage of Bike:", bike._mileage)
bike.travel(30)
print("Mileage after traveling 30 units with Bike:", bike._mileage)

# Calculate and print the least time to travel for both vehicles
distance_to_travel = 100
print("\nLeast time to travel 100 units with Car1:", car1.leastTimeToTravel(distance_to_travel), "minutes")
print("Least time to travel 100 units with Bike:", bike.leastTimeToTravel(distance_to_travel), "minutes")
