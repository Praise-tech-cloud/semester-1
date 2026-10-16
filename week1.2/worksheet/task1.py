# Worksheet 1.2: Task 1 Solution
import sys

try:
    grade = int(input("Give me a number from 0 to 100: "))
    if grade > 100 or grade < 0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    
    if grade >= 70:
        print(f" {grade} is a distinction")
    elif grade >= 40:
        print(f" {grade} is a pass")
    else:
        print(f" {grade} is a fail")

except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")
