# Module 5: Pandas (Reading CSV Files & Data Selection) 
import pandas as pd
#Task 2: CSV Practice 
# 1. Create a CSV file
data = {
    "Name": ["dilna", "vyga", "nandana"],
    "Marks": [80, 90, 85],
    "Grade": ["B", "A", "C"]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("CSV file created successfully!")

# 2. Read CSV using Pandas
data = pd.read_csv("students.csv")

# 3. Print the dataset
print("\nDataset:",data)

#Task 3: Column Selection 
# Read CSV file
df = pd.read_csv("students.csv")
print("Original Dataset:")
print(df)

# 1. Select a single column
print("\nSingle Column:")
print(df["Name"])

# 2. Select multiple columns
print("\nMultiple Columns:")
print(df[["Name", "Marks"]])

# 3. Print specific column values
print("\nSpecific Column Values:")

# Print the value at row 0 in the Name column
print(df["Name"].iloc[0])

#Task 4: Row Selection 
# 1. Select a row using loc
print("\nRow using loc:")
print(df.loc[1])

# 2. Select a row using iloc
print("\nRow using iloc:")
print(df.iloc[1])

# 3. Slice rows
print("\nSliced Rows:")
print(df.iloc[0:2])

#Task 5: Filtering
data = {
    "Name": ["dilna", "vyga", "nandana", "Maya"],
    "Marks": [80, 90, 85, 78],
    "City": ["chennai", "chennai", "Kochi", "Mumbai"]
}

df = pd.DataFrame(data)
# 1. Filter marks > 80
print("\nStudents with marks greater than 80:")
print(df[df["Marks"] > 80])

# 2. Filter city names
print("\nStudents from Kochi:")
print(df[df["City"] == "Kochi"])

# 3. Combine conditions
print("\nStudents from chennai with marks greater than 70:")
print(df[(df["City"] == "chennai") & (df["Marks"] > 70)])