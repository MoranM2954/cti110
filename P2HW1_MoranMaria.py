#Maria Moran
#June 19, 2025
#P2HW1
#This code contains changes to format output

budget_estimate = int(input("Enter budget:"))
travel_destination = (input("Enter your travel destination:"))

gas_expense = int(input("How much do you think you will spend on gas?:"))
accommodation_expense = int(input("Approximately, how much will you need for accommodations/hotel? :"))
food_expense = int(input("Lastly, how much will you need for food?:"))

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance= budget_estimate - total_expenses

print("This calculates and displays travel expenses.")
print("Enter budget:", budget_estimate)
print("Enter your travel destination:",   travel_destination)
print("\n --------------Travel Expenses--------------")
print("Travel destination:",  travel_destination)
print(f"Budget estimate:     ${budget_estimate: .2f}")
print(f"Gas:                 ${gas_expense: .2f}")
print(f"Accommodation:       ${accommodation_expense: .2f}")
print(f"Food:                ${food_expense: .2f}")
print("\n --------------------------------------------")
print(f"Remaining balance: ${remaining_balance: .2f}")
print("\n ")
