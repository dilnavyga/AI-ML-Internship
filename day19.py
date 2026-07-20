# NumPy (Operations – Part 2) 
import numpy as np
# Task 2: Arithmetic Practice 
a = np.array([1,2,3.8])
b = np.array([4,5,6])
# 1. Add two arrays 
print(a+b)  
# 2. Multiply arrays
print(a*b)  
# 3. Divide arrays 
print(a/b)

# Task 3: Scalar Operations 
# 1. Add constant to array 
print(a+2)  
# 2. Multiply array  
print(a*2) 
# 3. Subtract constant 
print(a/2) 

# Task 4: Math Functions
import math  
# 1. Find square root 
print(np.sqrt(b)) 

# 2. Find log values 
print(np.log(a)) 

# 3. Round values
print(np.round(a))
print(np.ceil(a))  
print(np.floor(a))

# Task 5: Aggregation 
# 1. Find sum
print(np.sum(b)) 

# 2. Find mean 
print(np.mean(b))  
# 3. Find max and min 
print(np.max(a))
print(np.min(a))

# Task 6: Axis Practice 
# 1. Row-wise sum 
ar = np.array([[1, 2, 3],[4, 5, 6]])
print(np.sum(ar,axis=1))  

# 2. Column-wise sum 
print(np.sum(ar, axis=0))

# Task 7: Filtering 
# 1. Filter values > 2  
print(a[a > 2])
# 2. Filter even numbers
print(a[a % 2==0])