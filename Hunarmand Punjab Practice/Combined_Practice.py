# Practice 1
name = "Maham Fayyaz"
age = 19
height = "5.2 feet"
country = "Pakistan"
goal = "AI Researcher"
print(f"My name is {name}, and I am {age} years old. My height is {height}, and I am from {country}. My goal is to become an {goal}.")

# Practice 2
student_name = "Maham Fayyaz"
father_name = "Muhammad Fayyaz"
age = 19
education = "ICS ECONOMICS"
city = "Sialkot, Pakistan"
favourite_subject = "Computer science"
college_name = "GOVT Graduate college for women Haji Pura sialkot"
print(f"My name is {student_name}. My father's name is {father_name}. I am {age} years old. I am studying {education}. I live in {city}. My favourite subject is {favourite_subject} and my college name is {college_name}.")

# Practice 3 — Simple Calculator

number1 = 20
number2 = 2
print("Addition:", number1 + number2)
print("Subtraction:",number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)
print("Power:", number1 ** number2)
print("Floor Division:", number1 // number2)

# Practice 4 Shoping Bill

item_name = "Note Book"
price = 450
quantity = 3
print("Item Name:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print(f"Toatl Bill : {price * quantity}")

# Practice 5 Age Calculator

birth_year = 2007
current_year = 2026
print(f"I am {current_year - birth_year} years old.")
# PRactice 6 student marks calculate
python = 85
computer = 80
math = 70
total_marks = python + computer + math
average = total_marks / 3
print(f"Total marks: {total_marks}")
print(f"Aveage:{average}")

#Practice 7 Temperature Converter
celsius = 30
print(f"Fahrenheight: {celsius * 9/5 + 32}")

# Practice 8 Type casting
price = "205"
quantity = 3
print(f"Total bill:{int(price) * quantity}")
#Practice 9 boolean
student = True
has_job = False
age = 19
print(student)
print(has_job)
print(age >= 18)
#Practice 10
python = 89
computer = 85
math = 85
total_marks = python + computer + math
average = total_marks / 3
print(total_marks)
print(average >= 50)
print(average)
#Practice 11 Function
# 1.
name = "Maham"
def introduce():
    print(f"My name is {name} Fayyaz.")
introduce()   
# 2.
name = "Muhammad Ali"
def intro():
    global name
    name = "Leon Jafri"
intro()
print(f"my name is {name}")
# Practice 12
my_list = ["Orange", "12", "Mango"]
x, y, z = my_list
print(x)
print(y)
print(z)
#Practice 13 dictionary
student ={
    "name" : "Lean jafri",
    "age" : 18,
    "height" : "5.2"
}
print(student)
print(student["name"])
print(student["age"])
print(student["height"])
#Practice 14 Typecasting+Boolean
age = "19"
height = "5.2"
print(int(age))
print(float(height))
print(int(age) <= 20)
print(float(height) >= int(age))
#Practice 15 Final practice
REPORT ={
    "name": "Leon Jafri",
    "Math": 80,
    "computer": 85,
    "python": 95,    
    "Total_marks": 80 + 85 + 95,
    "average": (80+85+95)/3,
    "pass_student": ((80+85+95)/3)>=50
}
print(REPORT["name"])
print(REPORT["Total_marks"])
print(REPORT["average"])
print(REPORT["pass_student"])
