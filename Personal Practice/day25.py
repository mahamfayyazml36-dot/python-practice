# My Day 25 Python Practice
# Name: Maham Fayyaz
# What I learned today: Higher-Order Functions & Function Manager
# (Functions as Arguments, Functions as Return Values, Nested Functions,
# Closures, Function Manager, Dynamic Function Execution,
# Parameters, Return Values, and Function Workflow)


# 1.
def introduction(name,father_name):
    print("Hello! " + "What is your name?")
    print("My name is " + name + " and my father name is " + father_name)
def execute_function(func, name,father_name):
    func(name,father_name)
execute_function(introduction, "Maham", "Muhammad Fayyaz.")

# 2.
def calculation(multiply, addition):
    multiplication = multiply * addition
    addition = multiplication + addition
    return multiplication, addition
def perform(total, multiply, addition):
    return total(multiply, addition)
result = perform(calculation, 58, 23)        
print(result)

# 3.
def square(number):
    return number * number
def excute(func, number):
    return func(number)
result = excute(square,45)
print(result)        

# 4.
def create_operation(operation):
    def calculation(first_number, second_number):
        if operation == "Multiply":
            return first_number * second_number
        elif operation == "add":
            return first_number + second_number
        elif operation == "subtraction":
            return first_number - second_number 
    return calculation
add = create_operation("add")
multiply = create_operation("Multiply")
subtraction = create_operation("subtraction")
print(add(45,850))                
print(multiply(5,4))
print(subtraction(9857.254,4579345.2341))

# Today's practice is complete.