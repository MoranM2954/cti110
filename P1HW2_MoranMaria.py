10#Maria Moran
#June 14, 2025
#P1HW2
#This program calculates and displays travel expenses

budget_estimate = int(input("Enter budget:"))
travel_destination = (input("Enter your travel destination:"))

gas_expense = int(input("How much do you think you will spend on gas?:"))
accommodation_expense = int(input("Approximately, how much will you need for accommodations/hotel? :"))
food_expense = int(input("Lastly, how much will you need for food?:"))

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance= budget_estimate - total_expenses

print("This calculates and displays travel expenses.")
print("Enter budget:", budget_estimate)
print("Enter your travel destination:", travel_destination)
print("\n ------Travel Expenses------")
print("Travel destination:", travel_destination)
print("Budget estimate:", budget_estimate)
print("\n ")
print("Gas:", gas_expense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print("\n ")
print("Remaining balance:", remaining_balance)
