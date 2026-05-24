# 1. Print your details (name, age, course) 

name = "Dilna"
age = 28
course = "AI-ML"
print("Name:", name)
print("Age:", age)
print("Course:", course)

# 2. Add, subtract, multiply two numbers  

a = 3
b = 5
print("addition=" ,a+b)
print("subtraction=" ,a-b)
print("multiplication=" ,a*b)

# 3. Check even or odd

# Check whether a number is even or odd

num = 3
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 4. Find largest of two numbers 

num1 = 3
num2 = 13
if num1 > num2:
    print("Largest number is:", num1)
else:
    print("Largest number is:", num2)  



#Task 3

# 1. Check whether number is positive, negative or zero
 
number = -3
if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# 2. Find largest of 3 numbers  

num1 = 23
num2 = 30
num3 = 13
if num1 > num2 and num1 > num3:
    print("Largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)  

# 3. Grade system:   

mark = 83
if mark > 90:
    print("Grade A")
elif mark >= 70 and mark <= 90:
    print("Grade B")
else:
    print("Grade C") 

# Task 4

# 1. Print numbers 1–20

for i in range(1, 21):
    print(i) 

#2. Print even numbers  

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#3. Print sum of first N numbers 

N = 10
total = 0
for i in range(1, N + 1):
    total += i
print("Sum =", total)

#4. Reverse numbers from 10 to 1  
 
for i in range(10, 0, -1):
    print(i)

# Task 5    

# 1.Function to add two numbers  

def add(a, b):     
    return a + b  
print(add(5, 3)) 

# 2. Function to check prime number 

def primecheck(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a Prime Number")
                break
        else:
            print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")

primecheck(3)

#3. Function to find factorial

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial =", fact)

factorial(5)
    
        
