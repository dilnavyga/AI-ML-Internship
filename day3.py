#Task 2
  
list_ = [1,2,3,4,5,6,7,8,9,10]

#Find sum of list elements
s = 0
for l in list_:
    s=s+l
print("sum = ",s)   

#Find maximum number  
max = list_[0]

for n in list_:
    if n > max:
        max = n
print("Maximum number = ", max)

#Print even numbers from list
for i in list_:
    if i%2==0:
     print(i)           

#Task 3
#Create student dictionary (name, age, marks)       
student = {"name": "Vyga","age": 20,"marks": 85}
print(student)

student["marks"] = 95

student["grade"] = "A"

for key, value in student.items():
    print(key, ":", value)

#Task 4

text = "Vyga"

count = len(text)
print("characters count:", count)  

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text    
print("Reversed:", reversed_text)

if reversed_text == text:
    print("palindrome")
else:
    print("not palindrome")  

count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print("vowels count:", count)

#Task 5
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = list(set(list1))
print("List without duplicates:", list1)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
common = set1.intersection(set2)
print("Common:", common)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x * x, numbers))
print("square",squares)

numbers = list(range(1, 21))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even numbers",even_numbers)


