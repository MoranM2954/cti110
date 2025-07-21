# Maria Moran
# July 7, 2025
# P4HW2
# The program will calculate gross pay for multiple employees

# Pseudocode
# Step 1 - Prompt user to enter employee information
# Step 2 - Calculate regular hours worked and overtime pay
# Step 3 - Calculate gross pay
# Step 4 - Display formatted results 


# Step 1 - Prompt user to enter employee information
total_regular_pay = 0.0
total_overtime_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
# Step 2 - Calculate regular hours worked and overtime pay using if/else statement
while employee_name != "Done":
    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter number of hours worked: "))

    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        overtime_worked = hours_worked - regular_hours

    else:
        regular_hours = hours_worked
        overtime_hours = 0
        
    # Step 3 - Calculate gross_pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
 # Step 4 - Display formatted results   
    print("-------------------------------------------------------------------------------------------")
    print(f"Employee name: {employee_name}" )
    print("                                                                                            ")
    print("Hours Worked   Pay Rate         Overtime        Overtime Pay     Regular Pay      Gross Pay" )
    print("--------------------------------------------------------------------------------------------")
    print(f"{hours_worked: <15.2f}${pay_rate: <15.2f} {overtime_worked: <15.2f} ${overtime_pay: <15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f} ")
    print("                                                                                            ")
    print()
    employee_name = input("Enter next employee's name or 'Done' to terminate: ")


print("--------------------------------------------------------------------------------------------")
print("                                                                   ")
print("Hours Worked   Pay Rate         Overtime        Overtime Pay     Regular Pay      Gross Pay" )
print("--------------------------------------------------------------------------------------------")
print(f"{hours_worked: <15.2f}${pay_rate: <15.2f} {overtime_worked: <15.2f} ${overtime_pay: <15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f} ")
print("                                                                              ")
print(f"Total Employee's Processed: {employee_count}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
