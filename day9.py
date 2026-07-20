#Task 2: File Data Practice 
# 1. Create file with student data 
students = []

# Read file
# 2. Read and store in list of dictionary
with open(r"C:\Users\Dilna\Desktop\AI-ML\AI_Python\students.txt", "r") as file:
    for line in file:
        name, mark = line.strip().split(",")

        students.append({
            "name": name,
            "mark": int(mark)
        }) 
  
# 3. Print all students 
print("Student Details:")
for student in students:
    print(student)
  
# 4. Find average marks
total = 0
for student in students:
    total += student["mark"]

average = total / len(students)
print("\nAverage Marks:", average)

# Find topper
topper = students[0]

for student in students:
    if student["mark"] > topper["mark"]:
        topper = student

print("Topper:", topper["name"], topper["mark"]) 

# Task 3: Data Processing Programs 
students = [
    {"name": "Dilna", "mark": 70},
    {"name": "Vyga", "mark": 95},
    {"name": "Nandana", "mark": 90},
    {"name": "Anu", "mark": 80},    
]

# 1. Filter students with marks > 75 
for student in students:
    if student["mark"] > 75:
        print(student["name"], student["mark"])  

# 2. Count number of students 
count = len(students)
print("Number of students:", count) 

# 3. Find lowest marks
lowest = students[0]
for student in students:
    if student["mark"] < lowest["mark"]:
        lowest = student

print("Lowest Marks:", lowest["name"], lowest["mark"])

# 4. Sort students by marks 
students.sort(key=lambda s: s["mark"])
for student in students:
    print(student)

# Task 4: Function Practice 
# 1. Function to calculate average
def average(students):
    total = 0
    for student in students:
        total += student["mark"]
    return total / len(students)

print("Average:", average(students))  

# 2. Function to find topper
def topper(students):
    top = students[0]
    for student in students:
        if student["mark"] > top["mark"]:
            top = student
    return top

result = topper(students)
print("Topper:", result["name"], result["mark"])  

# 3. Function to filter students 
def filter_students(students):
    for student in students:
        if student["mark"] > 75:
            print(student["name"], student["mark"])

filter_students(students)