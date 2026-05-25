#Task 2
# Create file and write your details

file = open("details.txt", "w")
file.write("Name: Vyga\n")
file.write("Place: calicut\n")
file.close()
print("Details written successfully")
    
# Read file and display

file = open("details.txt", "r")
content = file.read()
print(content)
file.close()   

# Append new data

file = open("details.txt", "a")
file.write("Age: 18\n")
file.write("Skill: Web Development\n")
file.close()
print("appended")

# Count number of lines

file = open("details.txt", "r")
lines = file.readlines()
count = len(lines)
print("lines count:",count)
file.close()

# 5. Count number of words

file = open("details.txt", "r")
content = file.read()
words = content.split()
wcount = len(words)
print("Number of words:",wcount)
file.close()

# Handle divide by zero

try:
    num1 = 3
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handle invalid input

try:
    num = int("v")
    print("You entered:", num)
except ValueError:
    print("Invalid input")  

# Use try-except-else-finally

try:
    num1 = 30
    num2 = 0

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")   

# Handle file not found error

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")         