# Kaggle - Intro to Programming
# Day 3: Data Types
# Topics Covered:
# - Integer Data Type (int)
# - Float Data Type (float)
# - Boolean Data Type (bool)
# - String Data Type (str)
# - type() Function
# - len() Function
# - Type Conversion (String to Float)
# - Basic Operations with Strings

# Data Types

# integer 

# 1.

x = 12
y = 3
print(x + y)
print(type(x))
print(type(y))

# Float

# 2.

a = 15.55
print(a)
print(type(a))

# 3.

z = 2.5256
print(z)
print(type(z))

y = 50/2
print(y)
print(type(y))

x = round(y, 5)
print(x)
print(type(x))
 
b = 250.
print(b)
print(type(b))

# Boolean

# 4. 

student = True
print(student)
print(type(student))

# 5.

numbers = 5 > 3
print(numbers)
print(type(numbers)) 

# 6.
has_job = False
print(has_job)
print(type(has_job))
# 7.
number = 5 < 3
print(number)
print(type(number))

# 8.
number1 = not number
print(number1)
print(type(number1))

# String

# 9.
intro = "Hello World!"
print(intro)
print(len(intro))
print(type(intro))
# 10.
quick = "1256.36"
print(quick)
print(float(quick))
print(type(quick))
# 11.
list_check = "ABC"*3
print(list_check)
# 12.

teen_age = "hhh" + "yyy"
print(teen_age)
print(type(teen_age))

# ============================================================
# DAY 3 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. Fundamental Data Types:
#    - int: Whole numbers (e.g., 12, 3).
#    - float: Decimal numbers (e.g., 15.55, 2.5256). Note: Division (/) always outputs float.
#    - bool: Logical True or False values (often generated via logical operations or 'not').
#    - str: Text enclosed in quotes (e.g., "Hello World!").

# 2. Key Built-in Functions Used:
#    - type(): Checks the data type of any variable.
#    - len(): Calculates string length (including spaces and symbols).
#    - round(): Rounds floats to a specified number of decimal places.
#    - float(): Converts string representation of numbers into actual float values.

# 3. String Manipulation Tricks:
#    - String Concatenation: Joining strings using '+' (e.g., "hhh" + "yyy").
#    - String Multiplication: Repeating strings using '*' (e.g., "ABC" * 3 -> "ABCABCABC").

# Status: All Kaggle Day 3 Concepts Covered & Successfully Tested!
# ============================================================