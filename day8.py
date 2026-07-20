# 1. Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))   
# 2. Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))  

# 3. Function to reverse string  
def reverse_string(text):
    return text[::-1]

print(reverse_string("agyv"))

# 4. Function to calculate average
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(average([10, 20, 30, 40, 50])) 

# Task 3: Recursion Practice 
# 1. Factorial using recursion 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 

# 2. Sum of numbers using recursion 
def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

print(sum_numbers(5)) 

# 3. Fibonacci series 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")

# Task 4: Lambda & Map 
# 1. Square all numbers 
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares) 

# 2. Double all values
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers))
print(double)  

# 3. Convert list to uppercase 
names = ["dilna", "vyga", "nandana"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names) 

# Task 5: Filter Practice 
# 1. Find even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  

# 2. Filter students with marks > 50  
students = [
    {"name": "Dilna", "mark": 45},
    {"name": "Vyga", "mark": 95},
    {"name": "Nandana", "mark": 90}
]

passed = list(filter(lambda s: s["mark"] > 50, students))

print(passed)

# 3. Filter words with length > 5
words = ["apple", "banana", "orange", "cat", "python"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)