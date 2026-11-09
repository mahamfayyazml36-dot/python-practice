# My Day 21 Python Practice
# Name: Maham Fayyaz
# What I learned today: Lambda Functions
# (Lambda Functions, Parameters, Arguments, Expressions,
# Automatic Return, String Transformation, and Conditional Lambda)


def calculation(a,b):
    addition = a + b
    return addition
result = calculation(12,30)
print(result)

multiply_by_ten = lambda number : number * 10
result = multiply_by_ten(10)
print(result)

table = lambda number : number * 11
result = table(9)
print(result)

square_number = lambda number : number * number
result = square_number(8)
print(result)

division = lambda first_number, second_number : first_number / second_number
result = division(415, 55)
print(result)

introduction = lambda name : name.upper()
result = introduction("maham fayyaz")
print(result)

check_age = lambda age : "Eligible" if age >= 18 else "Not Eligible" 
result = check_age(20)
result2 = check_age(14)
print(result)
print(result2)

# Today's practice is complete.
# I practiced using Lambda Functions for short and simple operations.
# I also practiced parameters, arguments, automatic return,
# string transformation, and conditional Lambda expressions.