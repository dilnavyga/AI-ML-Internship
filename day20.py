# Module 4: NumPy (Indexing & Slicing – Deep Dive)
import numpy as np
# Task 2: 1D Practice 
arr =  np.array([1,2,3,4,5,6,7,8])
# 1. Access first element 
print(arr[0]) 

# 2. Access last element 
print(arr[-1]) 

# 3. Slice array 
print(arr[1:6])

# Task 3: 2D Practice 
arr2 = np.array([[1,2,3],[4,5,6]])
# 1. Access element 
print(arr2[0, 1])  

# 2. Print row 
print(arr2[0])
  
# 3. Print column 
print(arr2[:,1])

# Task 4: 3D Practice 
# 1. Access layer 
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])  
# 2. Access row inside layer 
print("jj",arr3[1])  
# 3. Access single element
print(arr3[1][0][1])    

# Task 5: Slicing 
ar2s = np.array([[1,2,3],[4,5,6],[7,8,9]])
# 1. Extract sub-array
print(ar2s[0:2, 1:3])

# 2. Use step slicing  
print(ar2s[:, ::2])

# 3. Slice rows and columns 
print(ar2s[1:3, 0:2])

# Task 6: Boolean Indexing
arf = np.array([10, 20, 30, 40, 50, 60])  
# 1. Filter values > 25  
print(arf[arf  > 25])

# 2. Filter values between range
frange = arf[(arf >= 20) & (arf <= 50)] 
print(frange) 

# 3. Replace values conditionally 
arf[arf > 25] = 0 
print(arf)  