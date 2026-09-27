# My Mini Project 3: Simple Calculator
# Name: Maham Fayyaz
# What it does: Takes two numbers and performs addition, subtraction,
# multiplication, division, modulus, floor division, and power.
# What I learned: input(), float(), if-else, arithmetic operators
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

print("\n----Calculator Result----")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
    print("Floor division:", num1 // num2)
else:
    print("Division: Cannot divide by zero")   
    print("Modulus: Cannot divide by zero")
    print("Floor division: Cannot divide by zero")
print("Power:", num1 ** num2)     
# Mini Project day 3 complete.
# This calculator handles division by zero with an if-else check.