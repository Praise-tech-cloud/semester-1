# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

# multiply those numbers together
try:
    num1 = int(input("enetr a number"))
    num2 = int(input("enetr a number"))  
except ValueError: 
    print("That is not a number")
    exit()
# print out the result
    total = num1 * num2
    print(f"The total is {total}")

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!