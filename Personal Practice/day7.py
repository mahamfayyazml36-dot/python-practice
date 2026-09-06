'''# 🟢 DAY 7 — Conditions + Loops Integration
Part 1 — Conditions Deep Practice
if
if + else
if + elif + else
Multiple elif
Nested if
Multiple conditions
and
or
not
Comparison operators with real situations
Conditions with user input
Conditions with numbers
Conditions with strings
Conditions with lists
Part 2 — Condition Logic
Positive / negative / zero
Even / odd
Greater / smaller / equal
Multiple-number comparison
Range checking
Age/eligibility logic
Marks/grade logic
Login/validation logic
Combining multiple requirements
Part 3 — Conditions + Loops
for + if/elif/else
while + if/elif/else
Counting based on conditions
Filtering values using conditions
Searching using conditions
Accumulating values based on conditions
Nested conditions inside loops
Multiple conditions inside loops
Part 4 — Logic-Building Practice
Student marks analyzer
Grade calculator
Eligibility checker
Number analyzer
Simple data filtering
Multiple students processing
🟢 Part 5 — Day 7 Mini Project

Student Grade & Eligibility Analyzer

Ismein hum combine karenge:'''

# Practice 1
number = 10
if number > 5:
    print("Number is greater than 5")
else:    
    print("invalid")    
# Practice 2
marks = 75
if marks >= 50:
    print("Pass")   
else:
    print("Fail") 
# Practice 3
age = 20
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
# Practice 4
name = "Maham Fayyaz" 
if name == "Maham Fayyaz":
    print("Welcome", name)
else:
    print("Please try again")
#Practice 5
number = 10
if number == 10:
    print("Number is 10")   
else:
    print("Please try")
# Practice 6
number = 15
if number == 10:
    print("Number is 10")
else:
    print("Number is not 10") 
# practice 7
balance = 5000
if balance >= 1000:
    print("Sufficient balance")   
else:
    print(" Not Sufficient balance")                 
# Practice 8
temperature = 35
if temperature >= 30:
    print("It is not hot temperature")   
else:
    print("temperature is not hot")
# Practice 9
marks = 75
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B") 
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
# Practice 10
age = 20
if age >= 18:
    print("Adult")
elif age>= 13:
    print("Teenager")
else:
    print("Child")                           
# Practice 11
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero") 
# Practice 12
temperature = 25
if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Normal")
else:
    print("Cold")
# Practice 13
status = "pending"
if status == "active":
    print("Account is active") 
elif status == "pending":
    print("Account is pending")    
elif status == "blocked":
    print("Account is blocked")                              
else:
    print("Unknown status")
# Practice 14
amount = 7000
if amount >= 10000:
    print("20 Percent Discount")  
elif amount >= 5000:
    print("10 Percent Discount") 
elif amount >= 2000:
    print("5 Percent Discount") 
else:
    print("No Discount")   
# Practice 15 
marks = 45
attendance = 85
if marks >= 50 and attendance >= 75:
    print("Eligible")       
elif marks >= 50 and attendance < 75:
    print("Low Attendance")
else:
    print("Fail")
# Practice 16    
number= 15
if number > 0 and number %2 == 0:
    print("Positive Even")
elif number > 0 and number %2 != 0 :
    print("Positive Odd") 
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")            
# Practice 17
age = 20
if age >= 18:
    if age >= 21:
        print("Eligible for full driving category")
    else:
        print("Eligible for basic category")             
# Practice 18
marks = 75
attendance = 85
if marks >= 50:
    if attendance >= 75:
        print("Eligible")  
    else:
        print("Low Attendance")
else:
    print("Fail")        
# Practice 19
username ="Maham Fayyaz"
password = "1234" 
if username =="Maham Fayyaz":
    if password == "1234":
        print("Login Successful") 
    else:
        print("Wrong Password")                    
else:
    print("Wrong Username") 
# Practice 20
number= 10
if number > 0:
    if number %2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")           
# Practice 21
amount = 7000
member = True
if amount >= 5000:
    if member == True :
        print("Member Discount") 
    else:
        print("Regular Discount")  
else:
    print("No Discount")             
# Practice 22
marks = 85
if marks >= 50:
    if marks >= 80:
        print("Pass with Grade A")
    else:
        print("Pass")
else:
    print("Fail")
# Practice 23
account_active = True
balance = 5000
if account_active == True:
    if balance >= 1000:
        print("Transaction Allowed") 
    else:
        print("Insufficient Balance")                       
else:
    print("Account Inactive")        

# Practice 24
age = 22
student = True
if age >= 20:
    if student:
        print("Adult Student")    
    else:
        print("Adult Non-Student")  
else:
    print("Minor")          
# Practice 25
age = 16
if age < 18 or age > 60:
    print("appropriate")
else:
    print("Normal Age Group")     

# Practice 26
day = "sunday"       
if day == "sunday" or day == "saturday":
    print("Weekend")
else:
    print("Weekday")    
# Practice 27
marks = 85
if marks >= 80 or marks <= 50:
    print("Special Case")
else:
    print("Normal")
# Practice 28
logged_in = False
if not logged_in:
    print("Please login") 
else:
    print("Congratulation")
# Practice 29
account_active = False
if not account_active:
    print("Account is inactive")  
else:
    print("Account is active")
# Practice 30
student = True
if not student:
    print("Not a Student")      
else:
    print("Student")  
# Practice 31
age = int(input("Enter your age:"))                          
if age >= 18:
    print("Adult")
else:
    print("Minor")    
# Practice 32
marks = int(input("Enter your student marks:"))
if marks >= 50:
    print("Pass")
else:
    print("Fail") 
# Practice 33
number = int(input("Enter the number:"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
# Practice 34
fruits = ["apple", "banana", "mango"] 
if "mango" in fruits:
    print("True")
else:
    print("False")           
# Pratice 35
numbers = [10, 20, 30, 40, 50]
if 40 in numbers:
    print("Yes")
else:
    print("No")    
# Practice 36
students = ["Ali", "Sara", "Maham", "Ahmed"]
if "Sara" in students:
    print("True Present the Sara in this list")
else:
    print("Not present the Sara in this list")
# Practice 37
a = 10
b = 13
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a and b are equal")
# Practice 38
a = 5
b = 10
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a and b are equal")
# Practice 39
a = 15
b = 15
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a and b are equal")
# Practice 40
age = 20
if 18 <= age <= 30:
    print("Age is in the range 18 to 30")
else:
    print("Age is not in the range")
# Practice 41
marks = 80
if 50<= marks <= 100:
    print("marks is in the renge 50to 100")
else:
    print("marks is not in the range") 
# Practice 42
number = 25
if 10 <=  number <= 50:
    print("number is in the range 10 to 50")
else:
    print("number is not in the range")                

# Practice 43
numbers = [10, 15, 20, 25, 30] 
for number in numbers:
    if number % 2 == 0:
        print(number, "Even") 
    else:
        print(number, "Odd")      
# Practice 44
marks = [35, 55, 72, 45, 90]
for mark in marks:
    if mark >= 80:
        print(mark,"Grade A")
    elif mark >= 60:
        print(mark,"Grade B")
    elif mark >= 50:
        print(mark,"Grade C")
    else:
        print(mark,"Fail")
# Practice 45
numbers = [-5, 0, 10, -2, 8, 0]
for number in numbers:
    if number > 0:
        print(number, "positive")
    elif number < 0:
        print(number, "Negative")
    else:
        print(number, "Zero")  
# Practice 46
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number, "Even")
    else:
        print(number, "Odd")
    number = number + 1                                                  
# Practice 47
number = 1
while number <= 10:
    if number < 4:
        print(number,"Small") 
    elif 4<=number<=7: 
        print(number, "Medium")
    else:
        print(number, "Large")          
    number = number + 1    
# Practice 48
number = -5
while number <= 5:
    if number > 0:
        print(number, "Positive")
    elif number < 0:
        print(number, "negative")  
    else:
        print(number, "Zero")
    number = number + 1    
# Practice 49
numbers = [-5, 10, -2, 8, 0, 15, -7]
count = 0
for number in numbers:
    if number > 0:
        print(number,"Positive")
        count = count + 1
print("Positive Number:", count)
# Practice 50
marks = [35, 55, 72, 45, 90, 50, 40]
total = 0
for mark in marks:
    if mark >= 50:
        total = total + 1
print("Marks or 50 above:",total) 
# Practice 51
numbers = [-5, 10, -2, 8, 0, 15, -7]
for number in numbers:
    if number > 0:
        print("positive Number:", number)        
# Practice 52
marks = [45, 60, 75, 82, 90]
search = 75
for mark in marks:
    if mark == search:
        print("Number found")
# Practice 53
numbers = [-5, 10, -2, 8, 15, -7]
total = 0
for number in numbers:
    if number > 0:
        total =total + number
print("Total:", total)                    

# Practice 54
numbers = [5, 12, 20, 7, 30, 3]
for number in numbers:
    if number >= 10:
        if number >= 20:
            print(number,"Large")
        else:
            print(number,"Medium")    
    else:
        print(number,"Small")
# Practice 55
students = [
    ("Ali", 80),
    ("Sara", 45),
    ("Maham", 90)
]
for name, mark in students:
    if mark >= 50:
        if mark >= 80:
            print(name,"Excellent")
        else:
            print(name, "Pass")
    else:
        print(name,"Fail")                    
# Practice 56
ages = [12, 18, 25, 65, 30, 70]
for age in ages:
    if age >= 18 and age <= 60:
        print(age,"Eligible Age")
    else:
        print(age,"Not Eligible Age")    
# Practice 57
marks = [45, 65, 85, 30, 75]
for mark in marks:
    if mark >= 50 and mark <= 100:
        print(mark, "Pass")
    else:
        print(mark, "Fail")            
# Practice 58
marks = [45, 78, 32, 90, 65, 50, 88]
for mark in marks:
    if mark >= 80:
        print(mark, "Excellent") 
    elif mark >= 60:
        print(mark, "Good")
    elif mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")
# Practice 59
marks = int(input("Enter your student marks:"))

if marks >= 80:
    print(marks,"Grade A")
elif marks >= 70:
    print(marks, "Grade B")
elif marks >= 60:
    print(marks, "Grade C")
elif marks >= 50:
    print(marks, "Grade D")
else:
    print(marks, "Fail")
# Practice 60
ages = [15, 18, 22, 30, 65, 70]

for age in ages:
    if age >= 18 and age <= 60:
        print(age, "Eligible")
    else:
        print(age, "Not Eligible")
# Practice 61
numbers = [-5, 10, 0, -2, 7, 8, 15]

for number in numbers:
    if number > 0:
        if number % 2 == 0:
            print(number, "Positive Even")
        else:
            print(number, "Positive Odd")
    elif number < 0:
        if number % 2 == 0:
            print(number, "Negative Even")
        else:
            print(number, "Negative Odd")
    else:
        print(number, "Zero")
# Practice 62
marks = [35, 72, 45, 90, 55, 30, 85, 60]

for mark in marks:
    if mark >= 50:
        print(mark)
# Practice 63
students = [
    ("Ali", 85),
    ("Sara", 55),
    ("Maham", 92),
    ("Ahmed", 45),
    ("Ayesha", 70)
]

for name, mark in students:
    if mark >= 80:
        print(name, mark, "Excellent")
    elif mark >= 60:
        print(name, mark, "Good")
    elif mark >= 50:
        print(name, mark, "Pass")
    else:
        print(name, mark, "Fail")







