#Maria Moran
#June 21, 2025
#P2HW2
#Grade-book listing
#*****************************************************************
#Pseudocode
#Prompt user to enter grades for Module 1 through Module 6
#Store grades in the gradebook_grades list
#Find the lowest grade using min()
#Find the highest grade using max()
#Find the sum of the grades by using sum()
#Calculate the average by dividing the sum by the number of grades.
#Results should display the following: 
#     *Lowest grade
#     *Highest grade
#     *Sum of grades
#     *Average (Format to 2 decimal places)
#******************************************************************

#Step 1 - Enter grades into Grade-book
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

#Step 2 - Calculate values
lowest = min(gradebook_grades)
highest = max(gradebook_grades)
total = sum(gradebook_grades)
average = total / len(gradebook_grades)

#Step 3 -Display formatted results
print("\n --------------Results---------------------")
print(f"Lowest grade:      {lowest}")
print(f"Highest grade:     {highest}")
print(f"Sum of grades:     {total}")
print(f"Average:          {average: .2f}")
print("\n-------------------------------------------")
                     
               
               