# Task 2: JSON Practice 
# 1. Convert dictionary to JSON 
import json
dic = {"name":"vyga","id" : 4} 
j =  json.dumps(dic)
print(j)

# 2. Convert JSON to dictionary  
json_d = '{"name": "dilna", "id": 3}'
d = json.loads(json_d) 
print(d)

# 3. Write JSON to file 
with open("data.json", "w") as file: 
  json.dump(dic, file)  

# 4. Read JSON from file
with open("data.json", "r") as file: 
    data = json.load(file) 
print(data)    

# Task 3: CSV Practice 
# 1. Create CSV file  
# 2. Write student data 
import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"]) 
    writer.writerow(["vyga", 95]) 
    writer.writerow(["dilna", 80]) 
    writer.writerow(["nandana", 90]) 
print("CSV file created successfully.")
 
# 3. Read CSV file 
with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)  
# 4. Print formatted output 
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)      

    for row in reader:
        print(f"name: {row[0]}, mark: {row[1]} ")   

# Task 4: Combined Task 
# Program: 
# • Read CSV file 
# • Convert to dictionary  
# • Save as JSON 
 

students = []

# Read CSV file
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Save as JSON
with open("data.json", "w") as file:
    json.dump(students, file, indent=4)

print("CSV data converted to JSON successfully.")
