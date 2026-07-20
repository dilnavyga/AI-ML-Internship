# Task 2: Class Practice 
# 1. Create class Car with:  name, price   
# 2. Create object and print values  
class Car:
    name = ""
    price = 0

car1 = Car()
car1.name = "Toyota"
car1.price = 1200000

print(car1.name)
print(car1.price)

# Task 3: Constructor Practice 
# 1. Create class Student   
# 2. Initialize name and marks  
# 3. Print details 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Dilna", 80)
student1.display()

# Task 4: Method Practice 
# 1. Create method to:  
# o Check pass/fail  
# o Calculate grade 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

    def calculate_grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 75:
            print("Grade: B")
        elif self.marks >= 50:
            print("Grade: C")
        else:
            print("Grade: F")

student1 = Student("vyga", 95)

print("Name:", student1.name)
print("Marks:", student1.marks)

student1.check_result()
student1.calculate_grade()

# Task 5: Object List 
# 1. Create list of students   
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [
    Student("Dilna", 80),
    Student("Vyga", 95),
    Student("Nandana", 90),
    Student("Anu", 70),]

# 1. Print all students
print("Student Details:")
for student in students:
    print(student.name, student.marks)

# 2. Find topper
topper = students[0]

for student in students:
    if student.marks > topper.marks:
        topper = student

print("\nTopper:")
print(topper.name, topper.marks)
