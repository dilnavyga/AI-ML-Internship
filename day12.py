# Task 2: List Comprehension 
# 1. Square numbers 
num = [1,2,3,4,5]  
square = [n*n for n in num ]
print(square)

# 2. Find even numbers
even  = [n for n in num if n%2==0]   
print(even)

# 3. Convert strings to uppercase 
s = ["dilna","vyga"]
upper = [n.upper() for n in s ] 
print(upper)

# 4. Filter numbers > 50  
numbers = [20,60,30,55] 
filters = [f for f in numbers if f>50]
print(filters)

# Create number-square dictionary 
number = [1,2,3,4]
squaree = {n:n*n for n in number } 
print(squaree) 

# 2. Filter even numbers 
evenn = {n:n for n in number if n%2 == 0 }  
print(evenn)

# 3. Map names to lengths
names = ["dilna", "vyga", "nandana"]
name_length = {name: len(name) for name in names}
print(name_length)  

# Task 4: Set Practice 
# 1. Remove duplicates
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
unique_numbers = set(numbers)
print("Original List:", numbers)
print("Removing Duplicates:", unique_numbers)  

# 2. Find common elements 
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common = set1.intersection(set2) 
print("Common Elements:", common)

# 3. Find union and difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
difference_set = set1.difference(set2)
print("Union:", union_set)
print("Difference:", difference_set)

# Task 5: Generator Practice 
# 1. Create generator for numbers 
def number_generator():
    for i in range(1, 6):
        yield i
gen = number_generator()
for num in gen:
    print(num) 

# 2. Generate even numbers 
def even_number():
    for i in range(1,10):
        if i%2==0:
         yield i
e = even_number()  
for n in e:
    print(n)   

# 3. Fibonacci using generator 
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
gen = fibonacci(10)
for num in gen:
    print(num)  

# Task 6: Zip & Enumerate 
# 1. Combine 2 lists
a = [1,3,5,7]
b = [2,4,6,8] 
combine = list(zip(a,b))
print(combine) 

# 2. Print index + value 
fruits = ["Apple", "Banana", "Orange", "Grapes"]
for i,value in enumerate(fruits):
    print(i,value) 

# 3. Convert zip result to dictionary    
names = ["dilna", "vyga", "nandana"]
marks = [85, 95, 90]
student_marks = dict(zip(names, marks))
print(student_marks)