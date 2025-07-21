#Maria Moran
#June 27, 2025
#P3HW1
#This code must be debugged and completed. 
#This program takes a number grade , determines average and displays letter grade for average.

# Step 1 - Enter grades for six modules
gradebook_grades = []

grade1 = float(input("Enter grade for Module 1: "))
gradebook_grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
gradebook_grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
gradebook_grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
gradebook_grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: ")) 
gradebook_grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
gradebook_grades.append(grade6)

# Step 2 - Calculate grades
lowest = min(gradebook_grades)
highest = max(gradebook_grades)
total = sum(gradebook_grades)
average = total / len(gradebook_grades)

# Step 3 - Display formatted results
print("\n --------------Results---------------------")
print(f"Lowest grade:      {lowest}")
print(f"Highest grade:     {highest}")
print(f"Sum of grades:     {total}")
print(f"Average:          {average: .2f}")
print("\n-------------------------------------------")

# Step 4 - Display grade result                     
if average >= 90:
   print("Your grade is an: A")
elif average >= 80:
   print("Your grade is a: B")
elif average >= 70:
   print("Your grade is a: C")
elif average >= 60:
   print("Your grade is a: D")
else:
   print("Your grade is an: F") 
   


