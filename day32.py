# Module 6: Seaborn Introduction & Statistical Visualization
import matplotlib.pyplot as plt
#Task 2: Line Plot Practice
# 1. Create line graph
months = ["January", "February", "March", "April", "May"]
sales = [100, 120, 150, 130, 180]
plt.plot(months, sales)

# 2. Add style
plt.plot(months,sales,marker="o",linestyle="--")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.grid(True)

# 3. Compare data trends
months = ["January", "February", "March", "April", "May"]
sales_2025 = [100, 120, 150, 130, 180]
sales_2026 = [110, 140, 160, 150, 200]
plt.plot(months, sales_2025, marker="o", label="Sales 2025")
plt.plot(months, sales_2026, marker="s", linestyle="--", label="Sales 2026")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Trend Comparison")
plt.legend()
plt.grid(True)
plt.show()

#Task 3: Bar Plot Practice
# 1. Student marks comparison
students = ["dilna", "vyga", "nandana", "anu"]
marks = [80, 95, 90, 91]
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.show()

# 2. Sales comparison
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [100, 150, 120, 180]
plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Comparison")
plt.show()

# 3. Employee salary comparison
employees = ["Anu", "Binu", "Cathy", "David"]
salary = [30000, 45000, 40000, 55000]
plt.bar(employees, salary)
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.title("Employee Salary Comparison")
plt.show()

#Task 4: Scatter Plot Practice
# 1. Height vs weight
height = [150, 155, 160, 165, 170, 175]
weight = [50, 55, 60, 65, 70, 75]
plt.scatter(height, weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()

# 2. Study hours vs marks
study_hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 60, 65, 75, 85]
plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# 3. Temperature vs sales
temperature = [20, 22, 25, 28, 30, 35]
sales = [100, 120, 150, 180, 220, 300]
plt.scatter(temperature, sales)
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.title("Temperature vs Sales")
plt.show()

#Task 5: Histogram Practice
import random
# 1. Create histogram
data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 60]
plt.hist(data)
plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 2. Analyze frequency
data = [10, 12, 15, 18, 20, 22, 25, 25, 28, 30, 32, 35, 40, 45, 50]
plt.hist(data, bins=5)
plt.title("Frequency Analysis")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 3. Use random dataset
random_data = [random.randint(1, 100) for i in range(50)]
plt.hist(random_data, bins=10)
plt.title("Random Dataset Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#Task 6: Box Plot Practice
# 1. Detect outliers
data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 100]
plt.boxplot(data)
plt.title("Outlier Detection")
plt.show()

# 2. Analyze salary dataset
salaries = [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 150000]
plt.boxplot(salaries)
plt.title("Salary Analysis")
plt.ylabel("Salary")
plt.show()

# 3. Analyze marks dataset
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 95]
plt.boxplot(marks)
plt.title("Marks Analysis")
plt.ylabel("Marks")
plt.show()

#Task 7: Count Plot Practice 
# 1. Course count
courses = ["Python", "Java", "Python", "Django", "Java", "Python"]
plt.hist(courses)
plt.title("Course Count")
plt.xlabel("Courses")
plt.ylabel("Count")
plt.show()

# 2. Department count
departments = ["IT", "HR", "Sales", "IT", "HR", "IT"]
plt.hist(departments)
plt.title("Department Count")
plt.xlabel("Departments")
plt.ylabel("Count")
plt.show()

# 3. Product category count
categories = ["Electronics", "Clothing", "Electronics", "Food", "Clothing", "Electronics"]
plt.hist(categories)
plt.title("Product Category Count")
plt.xlabel("Product Categories")
plt.ylabel("Count")
plt.show()