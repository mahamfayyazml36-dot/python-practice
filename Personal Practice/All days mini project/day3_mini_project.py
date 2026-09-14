num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

print("\n----Calculator Result----")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("modulus:", num1 % num2)
    print("Floor division:", num1 // num2)
else:
    print("Division: Cannot divided by zero")   
    print("Modulus: Cannot divided by zero")
    print("Floor division: Cannot divided by zero")
print("Power:", num1 ** num2)     