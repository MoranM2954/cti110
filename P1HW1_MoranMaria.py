#The user should be able to enter any integer for the base value and the exponent.
base = int(input("Enter a base integer:"))
exponent = int(input("Enter an exponent integer:"))

num_1 = int(input("Enter the first integer:"))
num_2 = int(input("Enter the second integer:")) 
num_3 = int(input("Enter the third integer:")) 

sum_result = num_1 + num_2
final_result = sum_result - num_3
print(f"({num_1} + {num_2}) - {num_3} = {final_result}")