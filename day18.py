# Task 2: Array Creation

import numpy as np
# 1. Create 1D array 
ar1 =  np.array([1,2,3])  
# 2. Create 2D array  
ar2 = np.array([[1,2],[3,4]])
# 3. Create 3D array 
ar3 = np.array([[[1,2],[3,4]]])  
# 4. Print all 
print(ar1)
print(ar2) 
print(ar3)

# Task 3: Properties 
# 1. Print shape  
print(ar2.shape)
# 2. Print dimensions
print(ar2.ndim)   
# 3. Print data type 
print(ar2.dtype)

# Task 4: Special Arrays 
# 1. Create zero matrix 
zero_mx = np.zeros((3, 3))
print(zero_mx)

# 2. Create ones matrix 
ones_mx = np.ones((2, 3))
print(ones_mx)  

# 3. Create identity matrix 
identity_mx = np.eye(3)
print(identity_mx)  

# 4. Create range array 
range_array = np.arange(1, 10)
print(range_array)

# Task 5: Indexing  
arr = np.array([10, 20, 30, 40, 50,60]) 
# 1. Access first element
print(arr[0])

# 2. Slice array
print(arr[1:4])  

# 3. Access element in 2D  
print(ar2[0,1])

# Task 6: Reshaping 
# 1. Convert 1D → 2D  
arr2 = arr.reshape(2,3)
print(arr2)
# 2. Convert 2D → 1D
arr1 = arr2.flatten()
print(arr1)