# Module 4: NumPy (Random Module & Real Dataset Simulation) 
import numpy as np
# Task 2: Random Integer Practice 
# 1. Generate random integer  
print(np.random.randint(1,10,size=3))

# 2. Generate array of integers  
print(np.random.rand(2,3))

# 3. Create random matrix 
np.random.randint(1, 101, size=(3,3))  

# Task 3: Random Decimal Practice
# 1. Generate decimal values
decimal_values = np.random.rand(5)
print("hh",decimal_values)

# 2. Create 2D decimal matrix
decimal_matrix = np.random.rand(3,3) 
print(decimal_matrix)

# Task 4: Random Choice
colors = ["red", "blue", "green", "yellow"]
names = ["dilna", "vyga", "nandana", "theertha"]
# 1. Pick random color
random_color = np.random.choice(colors)
print(random_color)

# 2. Generate multiple choices
multiple_choices = np.random.choice(colors, size=3)
print(multiple_choices)

# 3. Simulate random names
random_names = np.random.choice(names, size=3)
print(random_names)

# Task 5: Shuffle
# 1. Shuffle array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled array:", arr)

# 2. Shuffle student IDs
student_ids = np.array([101, 102, 103, 104, 105])
np.random.shuffle(student_ids)
print("Shuffled student IDs:", student_ids)

# Task 6: Dataset  
# 1. Create marks dataset
marks = np.random.randint(0, 101, size=10)
print("Marks dataset:", marks)

# 2. Create attendance dataset
attendance = np.random.randint(50, 101, size=10)
print("Attendance dataset:", attendance)

# 3. Create random image matrix
image_matrix = np.random.randint(0, 256, size=(5, 5)) 
print(image_matrix)