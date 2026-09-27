# My Mini Project 4: Number Printer & Multiplication Table
# Name: Maham Fayyaz
# What it does: Takes a number and prints numbers from 1 to that number,
# then prints its multiplication table from 1 to 10.
# What I learned: input(), int(), for loop, range()
number = int(input("Enter your number:"))
print("\n----Number from 1 to", number, "----")
for a in range(1, number + 1):
    print(a)
print("----Multiplication Table of", number, "----") 
for a in range(1, 11):
    print(number, "X", a, "=", number * a)
# Mini Project day 4 complete.
# This program prints numbers and a multiplication table using for loop.