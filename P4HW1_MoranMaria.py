# Maria Moran
# July 6, 2025
# P4HW1
# Edit and enhance exiting (grade-book) program with a loop

# Pseudocode
# Prompt user to enter scores
# Create score list
# Create a loop to collect the number of scores the user enters
# Evaluate if the score is between 0 and 100
# Display results

# Step 1 - Prompt user to enter scores
num_scores = int(input("How many scores would you like to enter? "))

# Step - 2 Create score list 
student_scores = []

# Step 3 - Create a loop to collect scores user enters
for i in range(num_scores):
    valid_input = 0
    while valid_input == 0:
        score_input = input(f"Enter score #{i + 1}: ")
        try:
            score = float(score_input)
# Step 4 - Evaluate, between 0 and 100
            if 0 <= score <= 100:
                student_scores.append(score)
                valid_input = 1
            else:
                 print("Invalid score. Please enter a number between 0 and 100. ")

        except ValueError:
            print("Invalid input. Please enter a numeric value. ")

# Step 5 - Display results

print("\n *************Results*************")

lowest_score = min(student_scores)
print(f"\nLowest score: {lowest_score} ")  

scores_without_lowest = student_scores.copy()
scores_without_lowest.remove(lowest_score)
print(f"Scores after dropping lowest: {scores_without_lowest}")   

average_score = sum(scores_without_lowest) / len(scores_without_lowest)
print(f"Average of remaining scores: {average_score:.2f}")

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Letter grade: {grade}: ")

print("\n***********************************")