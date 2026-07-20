# Module 4: NumPy (Broadcasting – Very Important Concept) 
import numpy as np
# Task 2: Basic Broadcasting
arr = np.array([10, 20, 30, 40])  
# 1. Add scalar to array
add_result = arr + 5
print(add_result)

# 2. Multiply array with scalar
multiply_result = arr * 2
print(multiply_result)

# 3. Divide array by scalar
divide_result = arr / 10
print(divide_result)

# Task 3: Array Broadcasting
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

# 1. Add two compatible arrays
add_result = arr1 + arr2
print(add_result)

# 2. Multiply arrays
multiply_result = arr1 * arr2
print(multiply_result)

# Task 4: Shape Practice
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

# 1. Print shapes
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)

# 2. Check compatible shapes
if arr1.shape == arr2.shape:
    print("Shapes are compatible")
else:
    print("Shapes are not compatible")

# 3. Try incompatible shapes
arr3 = np.array([1, 2])
print("Shape of arr3:", arr3.shape)
if arr1.shape == arr3.shape:
    print("Shapes are compatible")
else:
    print("Shapes are incompatible")

# Task 5: 2D Broadcasting
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 1. Add scalar to matrix
add_result = matrix + 5
print(add_result)

# 2. Multiply matrix
multiply_result = matrix * 2 
print(multiply_result)

# 3. Normalize matrix values
normalized_matrix = matrix / np.max(matrix) 
print(normalized_matrix)    
 