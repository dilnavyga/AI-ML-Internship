# Module 6: Data Visualization Basics with Matplotlib 
import matplotlib.pyplot as plt

#Task 2: Line Plot Practice
# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create line graph
plt.plot(x, y)

# Add labels
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Add title
plt.title("Simple Line Graph")

# Display graph
plt.show()

#Task 3: Styling Graphs
# Line graph with marker and line style
plt.plot(
    x,
    y,
    marker="o",      # Add circle markers
    linestyle="--"   # Dashed line
)

# Add grid
plt.grid(True)

#Task 4: Bar Chart Practice
# 1. Student marks comparison 
students = ["dilna", "vyga", "nandana", "anu"]
marks = [80, 95, 90, 85]
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.show()

# 2. Sales comparison  
months = ["January", "February", "March", "April"]
sales = [10000, 15000, 12000, 18000]
plt.bar(months, sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Comparison")
plt.show()

# 3. Product comparison 
products = ["Laptop", "Phone", "Tablet", "Watch"]
prices = [60000, 30000, 20000, 10000]
plt.bar(products, prices)
plt.xlabel("Products")
plt.ylabel("Price")
plt.title("Product Price Comparison")
plt.show()  

#Task 5: Pie Chart Practice 
# 1. Department distribution
departments = ["HR", "IT", "Sales", "Marketing"]
employees = [10, 25, 15, 20]
plt.pie(employees, labels=departments, autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()

# 2. Expense analysis
expenses = ["Food", "Rent", "Travel", "Shopping"]
amounts = [5000, 12000, 3000, 4000]
plt.pie(amounts, labels=expenses, autopct="%1.1f%%")
plt.title("Expense Analysis")
plt.show()

# 3. Course popularity
courses = ["Python", "Java", "Data Science", "Web Development"]
students = [40, 25, 35, 30]
plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Popularity")
plt.show()

#Task 6: Scatter Plot Practice 
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
 