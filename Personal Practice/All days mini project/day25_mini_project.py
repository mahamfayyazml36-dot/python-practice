# My Day 25 Python Mini Project
# Name: Maham Fayyaz
# Project: Employee Salary Function Manager
# What I practiced today: Higher-Order Functions & Function Manager
# (Functions as Arguments, Functions as Return Values, Nested Functions,
# Closures, Function Manager, Dynamic Function Execution,
# Parameters, Return Values, and Function Workflow)


def create_salary_operation(operation):
    def calculation(monthly_salary,bonus,tax, performance_bonus):
        if operation == "add":
            return monthly_salary + bonus
        elif operation == "subtraction":
            return monthly_salary - tax
        elif operation == "performance":
            return monthly_salary + performance_bonus       
    return calculation        
addition = create_salary_operation("add")
subtraction = create_salary_operation("subtraction")
performance = create_salary_operation("performance")
while True:
    function_manager = {
        "add" : addition,
        "subtraction" : subtraction,
        "performance" : performance
    }
    operation = input("Enter Operation(add/subtraction/performance/exit): ")
    if operation == "exit":
        print("Salary Manager Closed.")
        break
    elif operation not in function_manager:
        print("Invalid operation!")
        continue
    else:
        selected_function = function_manager[operation]
        monthly_salary = float(input("Enter monthly salary: "))
        bonus = float(input("Enter bonus: "))
        tax = float(input("Enter tax: "))
        performance_bonus = float(input("Enter performance bonus: "))
        result = selected_function(
            monthly_salary,
            bonus,
            tax,
            performance_bonus
        )
        print("Final Salary:", result)


# Today's practice is complete.
# Day 25 completed successfully!