from rental import Vehicle, Renter, ElectricCar, Motorbike


print(" CampusWheels Vehicle Rental ")

car = Vehicle("Ford", "Mustang", "9E8862")
electric_car = ElectricCar("Tesla", "Model 7", "7C2365", 75)
motorbike = Motorbike("Ducati", "916", "3E321", 500)

print("\n--- Vehicles ---")
print(car)
print(electric_car)
print(motorbike)

print("\n--- Rent and Return ---")

car.rent()
print("After renting:")
print(car)

car.return_vehicle()
print("After returning:")
print(car)


# Create a renter
print("\n--- Renter ---")

renter = Renter("Reka", 12000)

print("Name:", renter.name)
print("License number:", renter.license_no)
print("Rented vehicles:", renter.rented)


# Test invalid renter name
print("\n--- Error Handling ---")

try:
    bad_renter = Renter("", 12000)
except ValueError as e:
    print("Invalid name:", e)


# Test invalid license number
try:
    bad_renter = Renter("John", 0)
except ValueError as e:
    print("Invalid license:", e)


# Test changing renter information
try:
    renter.name = ""
except ValueError as e:
    print("Invalid name when changing:", e)


try:
    renter.license_no = -10
except ValueError as e:
    print("Invalid license when changing:", e)


# Test inheritance
print("\n--- Inheritance ---")

print("ElectricCar is a Vehicle:", isinstance(electric_car, Vehicle))
print("Motorbike is a Vehicle:", isinstance(motorbike, Vehicle))


# Test that inherited methods work
electric_car.rent()
motorbike.rent()

print("\nElectric car after renting:")
print(electric_car)

print("Motorbike after renting:")
print(motorbike)


# Test polymorphism
print("\n--- Polymorphism ---")

vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)