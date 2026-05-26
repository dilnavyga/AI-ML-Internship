# Reverse a string

text = "vyga mol" 
rev = ""        

for char in text:
     rev = char + rev 

print(rev) 

#2. Count number of words

words = text.split()
count = len(words)
print(count)
  
if text == rev:
     print("Palindrome")
else:
    print("Not palindrome")

# 4. Replace words

new_text = text.replace("mol", "sasi")
print(new_text)     

#5. Count vowels  

count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print(count)

# Task 3

# 1. Create list of 5 students

students = [
    {"name": "Vyga", "marks": 95},
    {"name": "Dilna", "marks": 80},
    {"name": "Nandana", "marks": 90},
    {"name": "Theertha", "marks": 85},
    {"name": "Sharanya", "marks": 83}
]

# 2. Print all students

print("All Students:")
for s in students:
    print(s["name"], s["marks"])

# 3. Find average marks

total = 0
for s in students:
    total += s["marks"]
scount = len(students)
avg = total / count
print("Average Marks:", avg)

# 4. Find highest marks

highest = students[0]["marks"]
for s in students:
    if s["marks"] > highest:
        highest = s["marks"]
print("Highest Mark:", highest)

# 5. Print students with marks > 75

print("Students with marks > 75:")

for s in students:
    if s["marks"] > 85:
        print(s["name"], s["marks"])

#Task 4
# 1. Use math module
import math
print(math.sqrt(23))  

print(math.pow(2, 3))    

# Use random module
import random

print(random.randint(1, 10))

fruits = ["apple", "banana", "orange"]

print(random.choice(fruits))

# Create your own module 
import mymodule
mymodule.greet("vyga")