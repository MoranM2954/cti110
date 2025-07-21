#Maria Moran
#June 27, 2025
#P3HW2
#Calculate employee hours and pay then display formatted results.

#Pseudocode
#Prompt user to enter employee name, hours and pay rate
#Calculate regular hours worked 
#Calculate overtime pay
#Calculate gross pay
#Display formatted results 

#Step 1 - Prompt user to enter employee name, hours and pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter hours worked: "))
pay_rate = float(input("Enter employee's hourly pay rate: "))

#Step 2 - Calculate regular hours worked
regular_hours = 40

#Step 3 - Calculate overtime pay
overtime_rate = 1.5

if hours_worked > regular_hours:
    overtime_worked = hours_worked - regular_hours
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_worked * (pay_rate * overtime_rate )
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

#Step 4 - Calculate gross pay
gross_pay = overtime_pay + regular_pay

#Step 5 - Display formatted results
print("------------------------------------")
print("Employee name:", employee_name)
print("                                                                                ")
print("Hours Worked   Pay Rate         Overtime        Overtime Pay     Regular Pay      Gross Pay" )
print("--------------------------------------------------------------------------------------------")
print(f"{hours_worked: <15.2f}${pay_rate: <15.2f} {overtime_worked: <15.2f} ${overtime_pay: <15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f} ")
print("                                                                              ")
