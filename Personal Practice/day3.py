# ============================================================
# Python Practice - Day 3: Conditional Statements
#
# Practiced and completed by: Maham Fayyaz
# This practice was completed independently while learning
# Python programming.
#
# Topics Covered:
# - if Statement
# - if-else Statement
# - if-elif-else Statement
# - Nested if Statements
# - Nested if-else Statements
# - Nested if-elif-else Statements
# - Logical Operators with if
# - Using and, or and not with Conditions
# - Building Conditions for Real-World Examples
# ============================================================

# My Day 3 Python Practice


# if statement
age = 20
if age >= 18:
    print("your are adult!")

height = 5.2
if height <= 5.6:
    print("Nice your height!") 

age = 45
if age >= 40:
    print("Great!")

#if else statement
#1.
age = 16
if age >= 18:
    print("you can vote.") 
else:
    print("You can not vote!") 
#2.
marks = 850
if marks >= 750:
    print("you are intelligent student.")
else:
    print("normal marks")  
#3.
temperature = 52
if temperature >= 40:
    print("Today is hot!")
else:
    print("Today is cold!")  


# if elif else statement
marks = 85
if marks >= 90:
    print("Your grade: A")
elif marks >= 80:
    print("Your grade: B") 
elif marks >= 70:
    print("your grade: C")
else:
    print("You are fail!!!!")        

# Nested if
#1.
age = 25
voter = True
if age >= 18:
    if voter:
        print("you can enter in pak militry acadamy.")
#2.
temperature = 30
season_cold = True
if temperature <= 42:
    if season_cold:
        print("Today season is nice!")
#3.
marks = 85
attendence = 80
if marks >= 80:
    if attendence >= 50:
        print("Your progress is Excellent!") 
#4. 
ice = 50
rain = True               
if ice >= 12:
    if rain:
        print("Please you can go in home.")

# Nested if else
#1.
age = 18
voter = False
if age >= 18:
    if voter:
        print("You can  adult for voting like noonleague or tehrike-insaf")
    else:
        print("You need National Indentity Card" )
else:
    print("You are under 18.")
#2.
marks = 70
atendence = 80
if marks >= 50:
    if atendence >= 75:
        print ("you passed!")
    else:
        print("Your atendence is too low!") 
else:
    print("you failed")

#3.
weather = 20
rainy = False
if weather >= 20:
    if rainy:
        print("Weather is warm but rainy.")
    else:
        print("Weather is warm but cleaner.")                   
else:
    print("weather is too much cold.")
#Nested if elif else
#1.
model_prediction = "positive"
confidence = 0.86
if model_prediction == "positive":
    if confidence >= 0.90:
        print("Your model is too much high confidence")
    elif confidence >= 0.70:
        print("Medium confidence")
    else:
        print("Low confidence") 
else:
    print("Negative prediction your model") 
#2. 
price = 300000
if price >= 200000:
    if price >=500000:
        print("house is not afordable!")
    elif price >= 280000:
        print("Midum price house it's afordable!")
    else:
        print("cheap price house!")
else:
    print("Price is too low!") 

#🐍 Logical Operators with if
#1. and (dunu condition true huni chahiye)
model_accuracy = 92
model_ready = True
if model_accuracy >= 90 and model_ready: 
    print("Your model is ready for deployment!")
else:
    print("mdel need more work!") 
# 2. or (kam az kam aik condition True honi chahiye)
accuracy = 75
f1_score = 90
if accuracy >= 90 or f1_score >=85:
    print("Matrix condition good!")
else:
    print("Need more wor on model!") 
#3. not 
modelfailed = True
if not modelfailed:
    print("Model is good working!") 
else:
    print("Model is hectic")          
       
                     # HUNARMAND PYTHON — DAY 1
#Topic: print()

# Practice 1 — Basic print()

print("Assalam-o-alaikum!")                     
print("My name is Maham Fayyaz.")
print("I am learning Python.")
print("I want to become an AI Researcher.")

# Practice 2 

print("Height: 5.2")
print("Age: 19")
print("Birth Date: 1-March-2007")

# Practice 3

name = "Jannat Fayyaz"
age = 20
height = "5 feet"
print(name, age, height)

# Practice 4

name = "Noor salam"
age = 25
height = "5.5 feet"
education = "BS Mathematics"
print("My name is", name,"and I am", age,"years old.")
print("My height is", height,"and my education is", education,".")

# Practice 5

name = "Noor Salam"
age = 25
print("name")
print(name)
print("age")
print(age)

# Practice 6

number1 = 15
number2 = 5
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 ** number2)
print(number1 // number2)

# Practice 7

x = 10 
y = 2 
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** y)
print("Floor Division:", x // y)

# Practice 8

price = 50
quantity = 2
print("Price:", price)
print("Quantity:", quantity)
print("Total:", price * quantity)

# Prcatice 9

student_name = "Jannat"
father_name = "Fayyaz"
print(student_name + father_name)
print(student_name+ " " +father_name)

# Practice 10

first_name = "Maham"
second_name = "Fayyaz"
age = 19
height = 5.1
print("My first name is", first_name)
print("My second name is", second_name)
print("My age is", age)
print("My height is", height)

# Practice 11

name = "Maham"
age = 19
print(name, age)
print(name+ " " +str(age))

# Practice 12

name = "Laiba Imtiaz"
age = 18
height = "6 feet"
print(f"My cousin name,age is {name} {age} years old and height is {height}.")
             # Now Day 3 start
# Practice 1 variable + Assignment
name = "Gelbro"
age = 30
height = "45 qr"
company = True
print(name)
print(age)
print(height)
print(company)

# Practice 2 Basic Data Type
age = 19    # int
height = 5.2  # float
name = "Maham"  # string
student = True  #boolean
result = None   #None
print(age)
print(height)
print(name)
print(student)
print(result)

# Type
print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(result))

# Practice 3 Multiple variable
x, y, z = "Orange","Red", "Green"
print(x, y, z)
print(x)
print(y)
print(z)

# Practice 4 One Value → Multiple Variables
x = y = z = "Yellow"
print(x)
print(y)
print(z)

# Practice 5 Unpacking a collection List
shop = ["shoes","dress", "bag"]
x, y, z = shop
print(x)
print(y)
print(z)

# Practice 6 Unpacking a collection tuple
bag = ("pencil","ink", "blue pen")
a, b, c = bag
print(a)
print(b)
print(c)

# Practice 7 output variable
a1 = "She is"
b2 = 20
c3 = "years old."
print(a1, b2, c3)

x = "He is"
y = "25"
z = "years old."
print(x+" "+y+ " "+z)

# Practice 8 Function
# without parameter
def intro():
    print("My name is leon.")
intro()

#Practice 9 Global variable
introduction = "How are you class?"
def myfunc():
    print("Salam!" + introduction)
myfunc()    

#Practice 10 Global keyword
x = "I am learning Python"
def y():
    global x                # global keyword global variable ki  value ku change kr deta hai
    x = "My name is Maham Fayyaz."
y()
print("you know " + x)

# Practice 11 Local vs Global variable
name = "Maham"   #global variable
def y():
    name = "Muhammad ali"     #Local variable
    print("inside function:" "My name is " + name)
y()
print("Outside function:" "and my sister name is " + name)

# Practice 12 Data type int float string complex
a = 12
b = 12.2
c = "maham"
d = 3 + 4j
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Practice 13 List
fruits = ["Orange", "banana", "Apple"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Practice 14 Tuple + Range
# Tuple
shop = ("Green color", 25, "Orange")
print(shop)
print(type(shop))
print(shop[0])
print(shop[1])
print(shop[2])

# Range

number = range(0, 10)
print(number)
print(type(number))

#Practice 15 Dict
student ={
    "name" : "Maham",
    "age" : 19,
    "height" : "5.2 feet"
}
print(student)
print(type(student))
print(student["name"])
print(student["age"])
print(student["height"])

# Practice 16 
#Set
Apps = {"Orange", "Apple","banana", "Apple"}
print(Apps)
print(type(Apps))

#Practice 17 
#Frozenset
fruit = frozenset(["12", "Orange", "green"])
print(fruit)
print(type(fruit))

# Practice 18 
#Boolean
is_student = True
has_job = False
print(is_student)
print(type(is_student))
print(has_job)
print(type(has_job))

# Practice 19 
#Byte
y = b"Hello"
print(y)
print(type(y))

#Practice 20 
#Bytearray
y = bytearray(b"hello")
print(y)
print(type(y))

#Practice 21 
#memoryview
y = bytearray(b"hello")
view = memoryview(y)
print(view)
print(type(view))

#Practice 22 
#None
result = None
print(result)
print(type(result))

# Type casting
age = 19
height = 2.5
Age = "18"
print(str(age))
print(float(Age))
print(int(height))
print(type(str(age)))
print(type(float(Age)))
print(type(int(height)))
number1 = 1
print(bool(number1))
print(type(bool(number1)))
text = "hello"
print(bool(text))
print(type(bool(text)))
# ============================================================
# DAY 3 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. if Statement:
#    - Learned how to execute code when a condition is True.
#
# 2. if-else Statement:
#    - Learned how to execute different code depending on
#      whether a condition is True or False.
#
# 3. if-elif-else Statement:
#    - Practiced checking multiple conditions.
#    - Used it to create a simple grading system.
#
# 4. Nested if:
#    - Learned how to place one if statement inside another
#      if statement.
#
# 5. Nested if-else:
#    - Practiced multiple conditions using nested if and else
#      statements.
#
# 6. Nested if-elif-else:
#    - Practiced more complex decision-making using nested
#      conditions.
#
# 7. Logical Operators with if:
#    - Practiced 'and', 'or' and 'not' with conditional
#      statements.
#    - Used conditions with AI/ML examples such as model
#      accuracy, confidence and deployment readiness.
#
# 8. Practical Practice:
#    - Created different decision-making programs using
#      real-world examples such as age, marks, weather,
#      prices and AI model predictions.
#
# Status: Day 3 Conditional Statements Practice Completed Successfully!
# ============================================================       