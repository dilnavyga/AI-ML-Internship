# Module 4: NumPy (Reshaping & Array Manipulation)
import numpy as np
# Task 2: Reshape Practice 
# 1. Convert 1D → 2D  
ar1 = np.array([1,2,3,4,5,6,7,8,9,1,2,3])
ar2 = ar1.reshape(3,4)
print(ar2)
# 2. Convert 1D → 3D 
ar3 = ar1.reshape(2,2,3) 
print(ar3) 
# 3. Try invalid reshape 
#arv = ar1.reshape(3,5)

# Task 3: Flatten 
# 1. Convert 2D → 1D 
arr2 = np.array([[1,2,3],[4,5,6]])
flat = arr2.flatten()
print(flat)  

# 2. Compare flatten vs ravel  
rav = arr2.ravel()
print("Flatten:", flat)
print("Ravel:", rav)

# Task 4: Transpose 
# 1. Transpose matrix 
trance = ar2.T
print(trance)  
# 2. Verify rows columns 

# Task 5: Stacking 
# 1. Vertical stack  
arr1 = np.array([1, 2, 3])
arr3 = np.array([4, 5, 6])
print(np.vstack((arr1, arr2)))

# 2. Horizontal stack 
print(np.hstack((arr1, arr3)))  

# 3. Combine arrays  
print(np.concatenate((arr1, arr3)))

# Task 6: Splitting 
# 1. Split array 
ars = np.array([1,2,3,4,5,6]) 
print(np.split(ars, 3)) 

# 2. Split rows   
arrs = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(arrs,2))
