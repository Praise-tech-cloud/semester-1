# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")    

numbers.sort()
minimum = numbers[0]
maximum = numbers[- 1]
mean = sum(numbers)/len(numbers)

if len(numbers) % 2 == 0:
    median = (numbers[(len(numbers)//2) - 1] + numbers[(len(numbers)//2)]) / 2
else:
    median = numbers[len(numbers)//2]
print(f"Minimum = {minimum} ")
print(f"Maximum = {maximum} ")
print(f"Mean = {mean} ")
print(f"Median = {median} ")