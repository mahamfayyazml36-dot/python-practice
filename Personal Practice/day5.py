# My Day 5 Python Practice
# Name: Maham Fayyaz
# What I learned today: while loop, break, continue, pass, input validation
# Note: I wrote this code myself. Some comments and structure were helped by AI.

# Part 1: Basics
# Basic while loop
number = 1
while number <= 10:
    print(number)
    number = number + 1
# Counter / Increment +1, +2
numbers = 10
while numbers <= 15:
    print(numbers)    
    numbers = numbers + 2
# Decrement / Reverse counting
# Different step sizes
   
# 1
print("First")
number = 10
while number >= 1:
    print(number)
    number = number - 1
# 2
print("Second")
number2 = 20
while number2 >= 1:
    print(number2)
    number2 = number2 - 2
# 3 
print("Third")
count  = 15
while count >= 0:
    print(count)
    count = count - 3    
# 4
name = "Maham Fayyaz"
index = 0 
while index < len(name):
    print(name[index])
    index = index + 1
# 5
text = "HISTORY AND PYTHON"
numbers = 0
while numbers < len(text):
    if text[numbers] == "N": 
        print("N Found at position number:", numbers)
    numbers = numbers + 1    

# 6
number = int(input("Enter the first number:"))
while number >= 1:
    print(number)
    number = number - 1
# 7
number = 19
while number >= 1:
    print(number)
    number = number - 2   
# Infinite loop
'''number = 5

while number >= 1:
print(number)
# Infinite loop Fix       
count = 15
while count <= 20:
    print(count)
    count = count + 1'''      
# Infinite loop Break
# 1
while True:
    number1 = int(input("Enter your First number:"))
    number2 =int(input("Enter your second number:"))
    result = number1 + number2

    if result == 20:
        break 
    print(result)
print("Target Reached")    
# 2
while True:
    number = int(input("Enter the number:"))
    if number == 0:
        break
    print(number)    
print("Program stopped!")    
# 3
secret = 7
while True:
    number = int(input("Enter the number:"))
    if number == secret:
        print("Correct")
        break
    else:
        print("Try again")    
# 4
while True:
    number1 = int(input("Enter your number 1:"))
    number2 = int(input("Enter your number 2"))
    total = number1 + number2
    if total >= 50:
        print("Target reached!")
        break
    else:
        print("Try again!")
# 5
number = 1
while number <= 10:
    if number == 6:
        break
    print(number)
    number = number + 1
# 6
names = [
    ["maham", "Jannat", "maria"],
    ["python", "Nlp"]
] 
index = 0   
while index < len(names[0]):
    name = names[0][index]
    if name == "maham":
        print("Maham Found!")
        break
    index = index + 1

# 7
names = [
    ["Python", "Mlops", "Nlp"],
    [15, 20, 15, 20]
]
index =0
while index < len(names[1]):
    number = names[1] [index]
    if number == 15:
        index = index + 1
        print("Found 15")
        continue
    index = index + 1

# 8
counting = 20

while counting <= 25:
    if counting == 22:
        counting = counting + 1
        continue
    print(counting)
    counting = counting + 1
# 9 
while True:
    number = int(input("Enter your number:"))
    if number == 0:
        print("Number:",number)
        break
    elif number == 5:
        print("5 Skip")
        continue
    print("Number:", number)
# 10
words =["Python", "Nlp","Mlops", "Java", "Maham"] 
index = 0
while index < len(words):
    word = words[index]
    if word == "Java":
        index = index + 1
        continue
    print(word)
    index = index + 1  
# 11 
text = ["Data science", "AI", "AI ethics", "Machine Learning"]
number = 0
while number < len(text):
    My_list = text[number]
    if My_list == "AI":
        break
    print(My_list)
    number = number + 1 

# while with Boolean conditions
# 1
logged_in =True
while logged_in:
    print("User logged in ") 
    logged_in = False   
# 2
message_available = True
while message_available:
    print("New message received!")
    message_available = False
# 3
correct_password = "Python12356"
password_correct = False
while not password_correct:
    password = input("Enter your Password:")
    if password ==correct_password:
        print("Login successful.Your Password is correct.")
        password_correct = True
    else:
        print("Password is incorrect. Please try again!")    

# while + input()
# 1
while True:
    name =input("Enter your name:")
    if name == "Exit":
        break
    print(f"Hello! How are you {name}.")  
# 2 
while True:
    name = input("Enter your name:")
    if name == "exit":
        print("Program stopped!")
        break
    else:
        age =input("Enter your age:")
        print(name,"is", age,"years old.")
# 3 
number = int(input("Enter the First number:"))
while number <= 10 :
    print(number)
    number =number +1   
# 4
start = int(input("Enter the Starting number:"))
end = int(input("Enter the ending number:"))
while start <= end:
    print(start) 
    start = start + 1    
# 5
start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
step = int(input("Enter the Step Number:"))
while start <= end:
    print(start)
    start = start + step
# 6

number = int(input("Enter the number:"))
if number > 0:
    print("valid number")
else:
    print("Invalid number")    
# 7
while True:
    number = int(input("Enter the number:"))
    if number > 0:
        print("Valid number")
        break
    else:
        print("Invalid number")   
# 8
while True:
    number = int(input("Enter the number:"))
    if 1 <= number <= 100:
        print("Valid number")
        break
    else :
        print("Invalid number")            
# while + if/elif/else         
# 1
while True:
    user = input("Enter the status of user:")
    if user == "online":
        print("Please contact here")
        break
    elif user == "Offline":
        print("Please Don't call")
        break
    elif user == "busy":
        print("Please Don't disturb")
        break
    else:
        print("Invalid")    
# 2
correct_username = "Maham"
correct_password = "Python#@13"
password_username_correct =True
while password_username_correct:
    name = input("Enter the user name:")
    password = input("Enter the password:")
    if name == correct_username and password == correct_password:
        print("Login successful")
        password_username_correct = False
        break
    else:
        print("Invalid username and password!")

# 3
user_name = "My-dot"
email ="kijol123@gmail.com"
username_email = False
while True:
    username= input("Enter the user name:")
    emails = input("Enter the email:") 
    if username == user_name and emails == email :
        print("Valid")
        username_email = True
        break
    else:
        print("Invalid")    

# 4
correct_password = "Pythonhjhdasj#$@"
password_correct = False
while not password_correct:
    password = input("Enter the password:")
    if password == correct_password:
        print("Login successful")
        password_correct = True
        break
    else:
        print("Invalid!")
# Part 4
# 1
number = 1
while number <= 5:
    if number == 3:
        pass
    print(number) 
    number = number + 1       
# 2
numbers = 10
while numbers <= 15:
    if numbers == 14:
        pass
    print(numbers)
    numbers = numbers + 1
# 3
counter = 1
while counter <= 6:
    print("Hello Maham -", counter)
    counter = counter + 1
# 4
number = 15
total = 0
while number <= 18:
    total = total + number
    number = number + 1 
print("Total:", total)       

# Part 5
# 1
number = 2
while number <= 15:
    if number % 3 == 0:
        print(number)
    number = number + 1
# 2
number = 1
while number <=10:
    if number %2 == 0:
        print(number)
    number = number + 1    
# 3
number = 1 
while number <= 10:
    if number %2 != 0:
        print(number) 
    number = number + 1      
# 4 
number = 1
total = 0
while number <= 10:
    total = total + number
    number = number + 1
print("Total:", total)         


# 5
print("================================================")
print("Table of Five")
print("================================================")
number = 5
counter = 1
while counter <= 10: 
    print(number,"x",counter,"=", number*counter) 
    counter = counter + 1   
print("================================================")    



# Today's practice is complete.
# I learned while loop, break, continue, pass, input validation,
# counters, accumulators, even/odd logic, sum, and multiplication tables.