# Module 4: NumPy (Aggregations & Statistics)
import numpy as np
# Task 2: Basic Aggregation 
arr = np.array([10, 20, 30, 40, 50])
# 1. Find sum   
print(np.sum(arr))  

# 2. Find mean  
print(np.mean(arr))

# 3. Find max and min  
print(np.max(arr))
print(np.min(arr))

# Task 3: Statistical Functions 
arr = np.array([10, 20, 30, 40, 50])
# 1. Find median  
print(np.median(arr))

# 2. Find standard deviation
print(np.std(arr))

# 3. Find variance
print(np.var(arr))
 
# Task 4: Axis Practice
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])
# 1. Row-wise sum
row_sum = np.sum(arr, axis=1)
print("rowsum",row_sum)

# 2. Column-wise sum
column_sum = np.sum(arr, axis=0)
print("colsum",column_sum)

# 3. Mean using axis
row_mean = np.mean(arr, axis=1)
print(row_mean)
column_mean = np.mean(arr, axis=0)
print(column_mean)

# Task 5: Index Functions
arr = np.array([10, 20, 50, 30, 40])
# 1. Find index of max
max_index = np.argmax(arr)
print(max_index)

# 2. Find index of min
min_index = np.argmin(arr)
print(min_index)

# Task 6: Cumulative
arr = np.array([10, 20, 30, 40])
# 1. Compute cumulative sum
cumulative_sum = np.cumsum(arr)
print(cumulative_sum)