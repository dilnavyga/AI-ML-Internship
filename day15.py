# Task 2: Data Practice 
# Create list of marks
marks = [85, 90, 78, 88, 95]

# Find average
average = sum(marks) / len(marks)

# Find maximum and minimum marks
maximum = max(marks)
minimum = min(marks)

# Count total students
total_students = len(marks)

# Display results
print("Marks:", marks)
print("Average Marks:", average)
print("Maximum Marks:", maximum)
print("Minimum Marks:", minimum)
print("Total Students:", total_students)

# Task 3: Data Cleaning 
# Original data
data = [10, None, -5, 25, "abc", 40, None, -8, 50]

# Clean invalid data
clean_data = []
for item in data:
    if item is None:
        continue          # Remove None values
    elif type(item) != int:
        continue          # Remove invalid data (non-integer)
    elif item < 0:
        continue          # Remove negative values
    else:
        clean_data.append(item)

# Display results
print("Original Data:", data)
print("Clean Data:", clean_data)

# Task 4: Data Filtering 
# List of marks
marks = [45, 80, 67, 90, 75, 88, 50, 95]
# 1. Find passed students  
passed_students = []
for mark in marks:
    if mark >= 50:
        passed_students.append(mark)

# 2. Filter marks > 75 
greater_than_75 = []
for mark in marks:
    if mark > 75:
        greater_than_75.append(mark)

# 3. Filter even numbers  
even_numbers = []
for mark in marks:
    if mark % 2 == 0:
        even_numbers.append(mark)

# Display results
print("Marks:", marks)
print("Passed Students:", passed_students)
print("Marks > 75:", greater_than_75)
print("Even Numbers:", even_numbers)

# Task 5: Data Transformation 
# 1. Convert marks to percentage  
# 2. Multiply values  
# 3. Normalize data

