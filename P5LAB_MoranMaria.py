# Maria Moran
# July 12, 2025
# P5LAB
# This program will simulate a customer using a self-checkout machine.

# Pseudocode
# Convert change to cents
# Generate a random value for the total owed
# Ask user for payment
# Calculate change
# Call the main function

# Step 1 - Convert change to cents
import random

def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("Change owed: ")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

# Step 2 - Generate a random value for the total owed
def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

# Step 3 - Ask user for payment
    payment = float(input("Enter the amount of cash provided: $"))

# Step 4 -  Calculate change
    if payment < total_owed:
        print("Not enough money provided.")
    else:
        change = payment - total_owed
        print(f"Change to be returned: ${change:.2f}")
        disperse_change(change)
# Call main function
main()