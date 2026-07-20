#Task 2: List Problems 

l = [2,4,3,6,3,1,7]
#1. Find maximum and minimum
max = l[0]
min = l[0]
for i in l:
    if i > max:
        max = i
    if i < min:
        min = i     
print("maximium : ",max)
print("minimum : ",min) 

#2. Find second largest
l.sort()
print("second largest : ",l[-2])
   
#3. Remove duplicates
s = list[set(l)]
print(s)
   
#4. Count even and odd numbers
list = [2,4,3,6,3,1,7]
even = 0
odd = 0
for n in list:
    if n % 2 ==0:
        even+=1
    else:
        odd+=1
print("even count :",even) 
print("odd count : ",odd)  


# Task 3: String Problems 
text = "vygav" 
# 1. Reverse string 
slice = text[::-1]  
print("reversed : ",slice) 

# 2. Check palindrome
slice = text[::-1] 
if text == slice:
    print("paindrome")
else:
    print("not palindrome") 

# 3. Count characters
count = {}
for ch in text:
    count[ch] =  count.get(ch,0)+1
print(count)   

# 4. Count vowels and consonants  
vowel_c = 0
cons_c = 0
for ch in text:
    if ch in "aeiou":
         vowel_c+=1
    else:
        cons_c+=1
print("vowel count : ",vowel_c)
print("consonants count : ",cons_c) 


# Task 4: Dictionary Problems 
stlist =[{"name":"dilna","mark":80},
{"name":"vyga","mark":95},
{"name":"nandana","mark":90}]
# 1. Create student list
for student in stlist:
    print(student)
   
# 2. Find topper 
topper = stlist[0]
for student in stlist:
    if student["mark"] > topper["mark"]:
        topper = student
print("Topper:", topper["name"], topper["mark"])  
# 3. Calculate average
total = 0
for student in stlist:
    total += student["mark"]
average = total / len(stlist)
print("Average:", average)   
# 4. Filter passed students  
for student in stlist:
    if student["mark"] >= 50:
        print(student["name"], student["mark"])




   