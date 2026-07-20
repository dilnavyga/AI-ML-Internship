# Module 5: Pandas Introduction (Data Analysis Library)
import pandas as pd
# Task 2: Series Practice 
# 1. Create Series  
sr = pd.Series([1,2,3,4,5])
print(sr)

# 2. Create Series with custom index 
src = pd.Series([80,90,85],index=["dilna","vyga","nandana"])
print(src)  

# 3. Access Series values 
print("vygas mark : ",src["vyga"])

#Task 3: DataFrame Practice
# 1. Create a DataFrame using a dictionary
data =  {
    "name":["dilna","vyga","nandana"],
    "mark":[80,90,85]
}
df = pd.DataFrame(data)

# 2. Print the DataFrame
print("Original DataFrame:",df)
 
# 3. Add one more column
df["Grade"] = ["B", "A", "C"]
print("\nDataFrame after adding a column:",df)

# Task 4: Data Access   
# Create DataFrame
data = {
    "Name": ["Anu", "Riya", "Sara", "Maya"],
    "Marks": [80, 90, 75, 88],
    "Grade": ["B", "A", "C", "B"]
}
df = pd.DataFrame(data)
print("Original DataFrame:",df)
 
# 1. Access a single column
print("Single Column:")
print(df["Name"])

# 2. Access multiple columns
print("Multiple Columns:")
print(df[["Name", "Marks"]])

# 3. Print specific rows
print("\nSpecific Row:")
print(df.iloc[1])     

#Task 5: Data Information 
# 1. Use head()
print("First 5 rows:")
print(df.head())

# 2. Use tail()
print("\nLast 5 rows:")
print(df.tail())

# 3. Use info()
print("\nDataFrame Information:")
df.info() 
 