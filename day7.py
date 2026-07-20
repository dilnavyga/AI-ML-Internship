# Write program to check palindrome 
text = "vygagyv"
if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")     
    
# Find largest number in list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)  
  
# Count vowels in string 
text = "vyga"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowel count:", count)
  
# Create dictionary and print values
student = {
    "name": "vyga",
    "mark": 95,
    "course": "Python"
}
for value in student.values():
    print(value)

#Take 5 student inputs     
# students = []
# for i in range(5):
#     name = input("Enter student name: ")
#     mark = int(input("Enter mark: "))

#     students.append({
#         "name": name,
#         "mark": mark
#     })

# # Find average
# total = 0
# for student in students:
#     total += student["mark"]

# average = total / len(students)

# # Find topper
# topper = students[0]

# for student in students:
#     if student["mark"] > topper["mark"]:
#         topper = student

# print("\nAverage Mark:", average)
# print("Topper:", topper["name"], "-", topper["mark"])

# Task 1: Practice Problems 
# 1. Reverse list  
listt = [1,2,3,4,5,6]
rev = listt[::-1]
print(rev)
# 2. Count words in string 
text = "vygaa"  
count = {}
for ch in text:
    count[ch] = count.get(ch,0)+1
print(count)    

# 3. Remove duplicates
l = [1,2,3,4,3,5]
s = list[set(l)]
print(s)   
# 4. Find second largest 
l.sort()
print("second largest : ",l[-2])
