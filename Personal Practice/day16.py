# My Day 16 Python Practice 
# Name: Maham Fayyaz 
# What I learned today: Functions
# (Function Definition & Calling, Parameters & Arguments, 
# Multiple Parameters & Arguments, Return, ZeroDivisionError, 
# Default Parameters, Keyword Arguments, and previous concepts)

# Without Parameters func()
def welcome():
    print("Welcome to Python Functions")
welcome()    
# Parameters & Arguments
def introduce(name):
    print("Hello, my name is", name)
introduce("Maham Fayyaz")
# Multiple Parameters & Arguments
def introduction(boy_name, girl_name):
    print(boy_name ,": Excuse me, do I know you?")
    print(girl_name ,": Hassan? Is that really you?")
    print(boy_name,": Yes, that's me. But I'm sorry, I don't recognize you. Have we met before?")
introduction("Junaid", "Ayesha")

def subtraction(num1, num2):
    print("subtraction:", num1 - num2)
subtraction(20, 10)    
# function with return
def add(number1, number2):
    return number1 + number2
result = add(30, 10)
print("Addition:", result)    

def multiply(firstnumber, secondnumber):
    return firstnumber * secondnumber
result = multiply(25, 5)
print("Multiplication:", result)    

def division(num1, num2):
    return num1 / num2
result = division(50, 5)
print("Division:", result)    

def subtraction(num1, num2):
    return num1 - num2
result = subtraction(50, 23)
print("Subtraction:", result)     
# ZeroDivisionError
def division(num1, num2):
    if num2 == 0:
        print("Not possible division with zero")
    else:
        print("Division is possible")    
        return num1 / num2
    
result = division(50, 0)
print(result)
# Default Parameters
def greet(name = "Friend"):
    print("Hello", name)
greet()
greet("Maham")    

# Keyword Argument
def even(num1, num2):
    return num1 % num2 == 0
result = even(num2 = 2, num1 = 48)
print("Even:", result)

# Today's practice is complete. 
# I practiced Python functions with and without parameters, 
# multiple parameters and arguments, return values, 
# default parameters, keyword arguments, and basic error handling. 
# I also practiced using functions with arithmetic operations 
# and conditional statements.