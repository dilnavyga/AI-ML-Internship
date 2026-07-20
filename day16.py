# Task 2: Cleaning Practice 
# 1. Remove None values  
data = [10, None, 20, None, 30, 40]
c_none = [x for x in data if x is not None]
print(c_none)

# 2. Remove negative values
data = [10, -5, 20, -2, 30, 40]
c_negative = [x for x in data if x >= 0]
print(c_negative) 

# 3. Keep only valid data 
data = [85, -10, 90, None, 105, 75, 60]
valid_data = [x for x in data if x is not None and 0 <= x <= 100]
print(valid_data)

# Task 3: Transformation 
# 1. Add pass/fail field  
students = [
    {"name": "dilna", "marks": 80},
    {"name": "vyga", "marks": 95},
    {"name": "nandana", "marks": 90}
]
for student in students:
    if student["marks"] >= 85:
        student["result"] = "Pass"
    else:
        student["result"] = "Fail"
print(students)

# 2. Convert marks to percentage 
marks = [40, 35, 45]
percentage = [(mark / 50) * 100 for mark in marks]
print(percentage) 

# 3. Create new calculated field 
for student in students:
    student["percentage_"] = (student["marks"]/500)*100
print(student)
  
# Task 4: Sorting 
# 1. Sort students by marks 
sorted_st =sorted(students,
            key = lambda student : student["marks"],
            reverse=True)
print(sorted_st)
 
# 2. Print top 2 students 
top_2 = sorted_st[:2]
for student in top_2:
    print(student["name"], student["marks"])  

# Task 5: Grouping 
# 1. Group pass and fail 
groups = {
    "pass":[],"fail":[]
}  
for student in students:
    if student["marks"] >= 85:
        groups["pass"].append(student)
    else:
        groups["fail"].append(student) 
print(groups)  

# 2. Count each group  
print("pass :",len(groups["pass"]))  
print("fail :",len(groups["fail"]))  

# Task 6: Data Analysis 
# 1. Find average marks  
# 2. Find highest marks  
# 3. Find lowest marks
