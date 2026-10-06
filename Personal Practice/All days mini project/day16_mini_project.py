# My Mini Project 16: Mini Calculator 
# Name: Maham Fayyaz 
# What it does: Perform addition, subtraction, multiplication, division, 
# modulus, power, and floor division using Python functions. 
# What I learned: functions, parameters, arguments, return, input(), 
# int(), arithmetic operators, if-elif-else, and previous concepts.

first_number = int(input("Please Enter the First Number:"))
second_number = int(input("Please Enter the Second Number:"))
operation = input("Please Enter the Operation(+, -, /, *, %, **, //):")
def add(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number == 0:
        print("Division with Zero Not possible")
    else:
        return first_number / second_number

def modulus(first_number, second_number):
    if second_number == 0:
        print("Not possible by zero in modulus")
    else:    
        return (first_number % second_number)   

def power(first_number,  second_number):
    return(first_number ** second_number)

def floor_division(first_number, second_number):
    if second_number == 0:
        print("Floor division not possible by zero")
    else:    
        return first_number // second_number

if operation == "+":
    result = add(first_number, second_number)
    print("Addition:", result)
elif operation == "-":
    result = subtraction(first_number, second_number)
    print("Subtraction:", result)
elif operation == "*":
    result = multiplication(first_number, second_number)
    print("Multiplication:", result)
elif operation == "/":
    result = division(first_number, second_number)   
    print("Division:", result)
elif operation == "%":
    result = modulus(first_number, second_number)
    print("Modulus:", result)
elif operation == "**":
    result = power(first_number, second_number)
    print("Power:", result)
elif operation == "//":
    result = floor_division(first_number, second_number)
    print("Floor Division:", result)
else:
    print("Invalid your choice please rry again")            

# Mini Project Day 16 complete. 
# This program creates a Mini Calculator using Python functions. 
# It performs different mathematical operations based on the user's choice. 
# It uses functions, parameters, arguments, return values, 
# arithmetic operators, user input, conditional statements, 
# and basic error handling for division by zero.