#Maria Moran
#June 21, 2025
#P2LAB2
#Dictionary - how to write code that uses a dictionary to store user input and displays output to the user

print("\n --------------------MPG Dictionary-------------------------\n") 
mpg_dict= {
    "Camaro": 18.21, 
    "Prius": 52.36, 
    "Model S": 110, 
    "Silverado": 26,
    }
keys = mpg_dict.keys()            
print(keys)
print("\n")
vehicle = input("Enter the name of a vehcile from the list above:")
print("\n")
mpg = mpg_dict[vehicle]
print(f"The MPG for the vehicle {vehicle} is {mpg}.")
print("\n")

miles = float(input("Enter the number of miles you will drive:"))
print("\n")

gallons_needed = miles / mpg
print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} in a {vehicle}.")
print("\n")