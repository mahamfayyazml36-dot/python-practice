# Smart Calculator Project
# Created by: Maham Fayyaz
# Language: Python
# Topics: Input, Variables, Type Casting, Arithmetic Operators, If-Elif-Else, Error Handling

# This program takes two numbers from the user
# and performs different mathematical operations
# according to the selected operator.


print("=============SMART CALCULATOR=============")
number1 = int(input("Enter your First number:"))
number2 = int(input("Enter your Second number:"))
operation = input("Enter your Operation(+, -, *, /, //, **):") 
result = None
# Addition
if operation == "+":
    result = number1 + number2
# Subtraction
elif operation == "-":
    result = number1 - number2 
# Multiplication    
elif operation == "*":
    result = number1 * number2 
# Division
elif operation == "/":
    if number2 == 0:
        print("Message: Cannot divided by zero")
    else:    
        result = number1 / number2 
# Floor Division
elif operation == "//":
    if number2 == 0:
        print("Message: Cannot divided by zero")
    else:
        result = number1 // number2
# Power
elif operation == "**":
    result = number1 ** number2

else:
    print("Invalid number and Operation")
print("==================Full Result==================")                             
if result is not None:
    print("=============SMART CALCULATOR=============")
    print("First number:", number1)
    print("Second number:", number2)
    print("Operation:", operation)
    print(f"Result: {result:.2f}")
    print("==================Result==================")