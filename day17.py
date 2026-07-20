# Task 2: Math Practice 

import math
# 1. Find square root 
print(math.sqrt(25))
# 2. Find power
print(math.pow(2,5))  
# 3. Round numbers 
print(math.ceil(3.3))    # Round up 
print(math.floor(3.9))   # Round down   
# 4. Use π value  
print(math.pi)

# Task 3: Random Practice 
# 1. Generate random number 
import random
number = random.randint(1, 100)
print(number)  

# 2. Pick random element 
fruits = ["apple", "banana", "orange", "mango"]
random_ft = random.choice(fruits)
print(random_ft)  

# 3. Generate list of random numbers 
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)   

# Task 4: Datetime Practice 
# 1. Print current date
import datetime
now = datetime.datetime.now() 
print(now) 

# 2. Format date
print(now.strftime("%Y-%m-%d"))   

# 3. Extract year, month  
year = now.year
month = now.month
print("Year:", year)
print("Month:", month)

# Task 5: Visualization 
# 1. Create line graph 
import matplotlib.pyplot as plt

x = [2,4,6]
y = [20,40,60]
plt.plot(x,y)
plt.show()

# 2. Create bar chart  
plt.bar(x, y) 
plt.show() 

# 3. Plot student marks
students = ["dilna","vyga","nandana"]
marks = [80,95,90]
plt.plot(students,marks)
plt.show()