number = int(input("Enter your number:"))
print("\n----Number from 1 to", number,"----")
for a in range(1, number +1):
    print(a)
print("----Multiplication Table of", number,"----") 
for a in range(1, 11):
    print(number, "X", a, "=", number * a)
       