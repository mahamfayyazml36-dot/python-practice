# My Day 23 Python Mini Project
# Name: Maham Fayyaz
# Project: Scientific Calculation & Sequence Analyzer
# What I practiced today: Recursion
# (Recursive Functions, Base Case, Factorial, Fibonacci,
# Recursion vs Loops, and Recursion Limitations)

print("================================================================")
print("Scientific Factorial Calculator")
print("================================================================")
def scientific_factorial(number):
    if number == 1:
        return 1
    return number * scientific_factorial(number - 1)
result = scientific_factorial(50)
print("Scientific Factorial:", result) 
print("================================================================")
print("Fibonacci Sequence Generator")
print("================================================================")
def scientific_fibonacci(number):
    if number <= 1:
        return number
    return scientific_fibonacci(number - 1) + scientific_fibonacci(number - 2)
for number in range(15):
    print("Scientific Fibonacci:", scientific_fibonacci(number))
print("================================================================")
print("Scientific Results Analyzer")
print("================================================================")
even_count = 0
odd_count = 0
for number in range(15):
    fibonacci_result = scientific_fibonacci(number)
    if fibonacci_result % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("\nFactorial Result:", result)
print("Total Fibonacci Numbers:", 15)
print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)

print("\n******* Project Completed! *******")                    

# Today's mini project is complete.
# I practiced Recursion using Factorial Calculation,
# Fibonacci Sequence Generation, and Results Analysis.
# I also analyzed even and odd Fibonacci numbers.