# My Day 23 Python Practice
# Name: Maham Fayyaz
# What I learned today: Recursion
# (Recursion, Base Case, Factorial, Fibonacci, and Recursion vs Loop)

print("Recursion")
def countdown(number):
    if number == 1:
        print(number)
        return
    print(number)
    countdown(number - 1)
countdown(5)        

print("Factorial & recursion")
def factorial(number):
    if number == 1:
        print(number)
        return 1     # Base case
    return number * factorial(number - 1)
result = factorial(4)
print(result)       

print("Fibonacci Recursion")
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
for number in range(7):
    print(fibonacci(number))    

print("Fibonacci Recursion")
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
for number in range(10):
    print(fibonacci(number))        

print("Factorial & recursion")
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)
result = factorial(8)
print(result)

print("Recursion")
def recursion(number):
    if number == 1:
        print(number)
        return
    print(number)
    recursion(number - 1)
recursion(20)        
 
print("While Loop")
number = 5
while number >= 1:
    print(number)
    number = number - 1

# Today's practice is complete.