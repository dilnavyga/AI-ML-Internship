# Task 2: Debugging Practice 
#      Fix errors: 
# # Error 1 
# print("Hello 
print("vygamol")

# # Error 2 
# x = int("abc") 
x = int("123")

print(x) 
# # Error 3 
# nums = [1, 2, 3] 
# print(nums[5]) 
nums = [1, 2, 3]
print(nums[2])

# Task 3: Optimization Practice 
# 1. Replace loops with built-in functions
#before
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(total)
#after
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

# 2. Optimize sorting 
 
numbers = [50, 20, 10, 40, 30]
numbers.sort()
print(numbers)  
###
numbers = [50, 20, 10, 40, 30]
sorted_numbers = sorted(numbers)
print("Original:", numbers)
print("Sorted:", sorted_numbers)

# 3. Reduce repeated code 
student1 = 80
student2 = 90
student3 = 85
print(student1)
print(student2)
print(student3) 
###
students = [80, 90, 85]
for mark in students:
    print(mark) 

# Task 4: Refactoring 
#      Convert: 
# • Long code → functions 
a = 10
b = 20
print("Sum:", a + b)
a = 30
b = 40
print("Sum:", a + b) 
###
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)
add_numbers(30, 40)
 
# • Repeated logic → reusable function
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
###    
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check_even_odd(4)
check_even_odd(7)
       



