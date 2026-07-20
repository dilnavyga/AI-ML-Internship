#Module 5: Pandas (Sorting, Grouping & Data Analysis)
import pandas as pd  
#Task 2: Sorting Practice
# Create DataFrame
data = {
    "Name": ["dilna", "vyga", "nandana", "anu"],
    "Salary": [50000, 70000, 65000, 55000],
    "Department": ["IT", "HR", "IT", "HR"]
}
df = pd.DataFrame(data)

# 1. Sort salary in ascending order
print("\nSalary Ascending:")
print(df.sort_values(by="Salary"))

# 2. Sort salary in descending order
print("\nSalary Descending:")
print(df.sort_values(by="Salary", ascending=False))

# 3. Sort by multiple columns
print("\nSort by Department and Salary:")
print(df.sort_values(by=["Department", "Salary"],
                   ascending=[True, False]))

#Task 3: Grouping Practice
import pandas as pd

# Create DataFrame
data = {
    "Name": ["dilna", "vyga", "nandana", "anu", "aloka"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "City": ["Kochi", "Delhi", "Kochi", "Mumbai", "Delhi"],
    "Category": ["A", "B", "A", "B", "A"],
    "Salary": [50000, 60000, 55000, 65000, 70000]}
df = pd.DataFrame(data)
 
# 1. Group by Department
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# 2. Group by City
print("\nAverage Salary by City:")
print(df.groupby("City")["Salary"].mean())

# 3. Group by Category
print("\nAverage Salary by Category:")
print(df.groupby("Category")["Salary"].mean())

import pandas as pd

# Create DataFrame
data = {
    "Name": ["dilna", "vyga", "nandana", "anu", "aloka"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 60000, 55000, 65000, 70000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

#Task 4: Aggregation Practice
# 1. Find average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# 2. Find total salary
total_salary = df["Salary"].sum()
print("Total Salary:", total_salary)

# 3. Count employees
employee_count = df["Name"].count()
print("Number of Employees:", employee_count)

#Task 5: Multiple Aggregation
# Create DataFrame
data = {
   "Name": ["dilna", "vyga", "nandana", "anu", "aloka"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 60000, 55000, 65000, 70000]
}
df = pd.DataFrame(data)

# Multiple aggregations
result = df.groupby("Department")["Salary"].agg(
    ["mean", "max", "min"])
print(result)

# Create DataFrame
data = {
    "Name": ["Anu", "Riya", "Sara", "Maya", "Asha", "Neha"],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "IT"],
    "Category": ["A", "B", "A", "B", "A", "C"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

#Task 6: Value Counts 
# 1. Count departments
print("\nDepartment Counts:")
print(df["Department"].value_counts())

# 2. Count repeated values
print("\nRepeated Department Values:")
print(df["Department"].value_counts())

# 3. Analyze category frequency
print("\nCategory Frequency:")
print(df["Category"].value_counts())