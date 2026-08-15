# Student Report Card Project
# Created by: Maham Fayyaz
# Language: Python
# Topics: Input, Variables, Type Casting, Calculations, If-Else

name = input("Enter Your Student Name:")
father_name = input("Enter Your Father Name:")
class_ = input("Enter Your Class:")
roll_number = input("Enter Your Roll Number:")

english = int(input("Enter Your Marks of English:"))
math = int(input("Enter Your Marks of Math:"))
physics = int(input("Enter your Marks of Physics:"))
computer = int(input("Enter Your Marks of Computer:")) 
total = english + math + physics + computer
average = total / 4
percentage = (total / 400) * 100
print("==============Student Report Card==============")
print("Student Name:", name)
print("Father Name:", father_name)
print("Class:",class_)
print("Roll Number:", roll_number)

print("English Marks:", english)
print("Math Marks:", math)
print("Physics Marks:", physics)
print("Computer Science:", computer)
print("Total Marks:", total)
print("Average:", average)
print(f"Percentage {percentage:.2f}%")

if percentage >= 80:
    print("Your Grade is A")
    print("status: Passed!") 
elif percentage >= 70:
    print("Your Grade is B")
    print("status: Passed!") 
elif percentage >= 60:
    print("Your Grade is C")
    print("status: Passed!")   
else:
    print("Your Grade is: F") 
    print("Failed!")        
print("========== RESULT GENERATED SUCCESSFULLY ==========")