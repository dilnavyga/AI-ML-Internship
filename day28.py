# Module 5: Pandas (Handling Missing Data & Data Cleaning)
import pandas as pd  
#Task 2: Missing Data Practice

# 1. Create a dataset with missing values
data = {
    "Name": ["vyga", "dilna", "nandana", "anu"],
    "Marks": [80, None, 75, 90],
    "City": ["Kochi", "chennai", None, "Mumbai"]
}
df = pd.DataFrame(data)

# 2. Detect missing values
print("\nMissing Values:")
print(df.isnull())

# 3. Count missing values
print("\nCount of Missing Values:")
print(df.isnull().sum())

#Task 3: Remove Missing Data
# 1. Drop rows with missing values
rows_removed = df.dropna()
print("\nAfter dropping rows with missing values:")
print(rows_removed)

# 2. Drop columns with missing values
columns_removed = df.dropna(axis=1)
print("\nAfter dropping columns with missing values:")
print(columns_removed)

#Task 4: Fill Missing Data
# 1. Fill missing values with text
df["City"] = df["City"].fillna("Unknown")
print("\nAfter filling text:",df)

# 2. Fill missing values with mean value
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print("\nAfter filling Marks with mean:",df)
 
# 3. Fill numeric columns

#Task 5: Duplicate Handling 
datad = {
    "Name": ["dilna", "vyga", "nandana", "dilna"],
    "Marks": [80, 90, 75, 80],
    "City": ["calicut", "chennai", "kochi", "calicut"]
}
df = pd.DataFrame(datad)

# 2. Detect duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

# 3. Remove duplicate rows
df_cleaned = df.drop_duplicates()
print("\nAfter Removing Duplicates:") 
print(df_cleaned) 

#Task 6: Column Operations 
# 1. Rename columns
df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Student_Marks"
})
print("\nAfter Renaming Columns:",df)
 
# 2. Change data type
df["Student_Marks"] = df["Student_Marks"].astype(int)
print("\nAfter Changing Data Type:",df)
 
# 3. Print data types
print("\nData Types:")
print(df.dtypes)