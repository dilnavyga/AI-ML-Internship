#Module 6: Correlation, Heatmaps & Pairplots in Seaborn 
import pandas as pd
# 1. Create dataset
#Task 2: Correlation Practice 
data = {
    "Study Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 60, 65, 75, 85],
    "Sleep Hours": [8, 7, 7, 6, 6, 5]}
df = pd.DataFrame(data)

# 2. Find correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# 3. Analyze relationships
print("\nCorrelation between Study Hours and Marks:")
print(df["Study Hours"].corr(df["Marks"]))
print("\nCorrelation between Study Hours and Sleep Hours:")
print(df["Study Hours"].corr(df["Sleep Hours"]))

#Task 3: Heatmap Practice
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Create heatmap
data = {
    "Study Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 60, 65, 75, 85],
    "Sleep Hours": [8, 7, 7, 6, 6, 5]
}
df = pd.DataFrame(data)
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
# 2. Show annotations
plt.title("Correlation Heatmap")
plt.show()
# 3. Analyze strong correlations
print(correlation_matrix)

#Task 4: Pairplot Practice
df = pd.DataFrame(data)
sns.pairplot(df)

#Task 5: Scatter Plot Practice
# 1. Study hours vs marks
study_hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 60, 65, 75, 85]
plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# 2. Salary vs experience
experience = [1, 2, 3, 4, 5, 6]
salary = [25000, 30000, 35000, 42000, 50000, 60000]
plt.scatter(experience, salary)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()

# 3. Temperature vs sales
temperature = [20, 22, 25, 28, 30, 35]
sales = [100, 120, 150, 180, 220, 300]
plt.scatter(temperature, sales)
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.title("Temperature vs Sales")
plt.show()

#Task 6: Dataset Analysis
# 1. Student dataset
student_data = {
    "Name": ["Anu", "Binu", "Cathy", "David"],
    "Marks": [85, 72, 90, 65],
    "Study Hours": [5, 3, 6, 2]
}
students = pd.DataFrame(student_data)
print(students)
print(students.describe())

# 2. Employee dataset
employee_data = {
    "Name": ["Anu", "Binu", "Cathy", "David"],
    "Department": ["IT", "HR", "Sales", "IT"],
    "Salary": [50000, 40000, 45000, 60000]
}
employees = pd.DataFrame(employee_data)
print(employees)
print(employees.describe())

# 3. Hospital dataset
hospital_data = {
    "Patient": ["A", "B", "C", "D"],
    "Age": [25, 40, 35, 60],
    "Temperature": [98.6, 99.2, 100.1, 101.5]
}
hospital = pd.DataFrame(hospital_data)
print(hospital)
print(hospital.describe())