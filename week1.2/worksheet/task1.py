# Worksheet 1.2: Task 1 Solution
import sys

grade = int(input("Give me a number from 0 to 100: "))
try:
    if grade > 100:
        print("Error: Grade must be an integer between 0 and 100")
        sys.exit("Error!")
    elif grade >= 70:
        print(f" {grade} is a distinction")
    elif grade >= 40:
        print(f" {grade} is a pass")
    else:
        print(f" {grade} is a fail")
except ValueError:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit("Error!")
