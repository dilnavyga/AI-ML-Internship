# Module 4: NumPy (Real-World Problems & Practice)
import numpy as np
# Task 2: Marks Analysis 
arr = np.array([[80,73,85],[90,95,89],[85,90,93]])
# 1. Find average marks 
print("average",np.mean(arr)) 

# 2. Find highest marks
print("max",np.max(arr)) 

# 3. Find lowest marks 
print("min",np.min(arr))

# 4. Find topper  
total = np.sum(arr,axis = 1)
top = np.argmax(total)
print("topper:",top)

# Task 3: Image Operations
image = np.array([
    [50, 100, 150],
    [80, 120, 200],
    [30, 90, 180]
])
# 1. Increase brightness
bright_image = image + 50
print("Increased brightness:",bright_image) 

# 2. Decrease brightness
dark_image = image - 50
print("Decreased brightness:",dark_image) 

# 3. Normalize image pixels
normalized_image = image / np.max(image)
print("Normalized image:",normalized_image)
 
# Task 4: Dataset Filtering 
arf = np.array([30,50,60,40,80,90,70])
# 1. Filter values > 50  
filt = arf[arf > 50]
print("filterd :",filt)

# 2. Replace low values 
arf[arf < 50] = 50
print("replace",arf) 

# 3. Count filtered values  
count = np.sum(arf > 50)
print("count",count)

# Task 5: Reshaping 
# 1. Convert 1D → 2D  
ar1 = np.array([1,2,3,4,5,6])
ar2 = ar1.reshape(2,3)
print("2dary",ar2)
# 2. Convert 2D → 1D 
arr1 = ar2.flatten()
print("1dary",arr1)  
# 3. Create 3D dataset  
ar3 = np.array([[[50,20,90],[80,20,40]],[[70,50,60],[20,80,60]]])
print("3ddata",ar3)

# Task 6: Dataset Simulation 
# 1. Attendance matrix
attendance = np.random.randint(0,1,size=(5,7)) 
print("attendance",attendance)
# 2. Marks dataset
marks = np.random.randint(0, 101, size=10)
print("Marks dataset",marks) 

# 3. Weather dataset
temperature = np.random.randint(20, 41, size=7)
print("Weather dataset",temperature)
 

 