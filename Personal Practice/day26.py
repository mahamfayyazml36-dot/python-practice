# My Day 26 Python Practice
# Name: Maham Fayyaz
# What I learned today: List Comprehension & Data Transformation
# List Comprehension, Filtering, Conditions, Nested Lists,
# Data Transformation, Grade Classification

numbers= [1,2,3,4,5]
squares = [number ** 2 for number in numbers]
print(squares)

prices = [100,200,300,400,500]
new_prices = [number * 1.10 for number in prices]
print(new_prices)

name = ["ali", "sara", "maham", "jannat"]
names = [intro.upper()for intro in name]
print(names)


numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = [number for number in numbers if number % 2 == 0]
print(even_number)

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
even_square = [numbers ** 2 for numbers in number if numbers % 2 == 0]
print(even_square)

numbers = [2,4,6,8,10]
square = [number * 5 for number in numbers]
print(square)

numbers = [1,2,3,4,5,6,7,8,9,10,11]
odd_number = [number for number in numbers if number %2 != 0]
print(odd_number)

number = [1,2,3,4,5,6,7]
cube_number = [numbers ** 3 for numbers in number if numbers %2 == 0]
print(cube_number)

number = [23,22,21,20,19,18,17,16]
result =[]
for numbers in number:
    if numbers %2 == 0:
        result.append("Even")
    else:
        result.append("Odd")
print(result)

numbers = [23,22,21,20,19,18,17,16]
even_odd_number = ["Even" if number %2 == 0 else "Odd" for number in numbers]
print(even_odd_number)

marks = [95,85,80,75,70,50,40]
grades = [
    "A" if mark >= 85
    else "B" if mark >= 70
    else "C" if mark >= 50
    else "Fail"
    for mark in marks
]
print(grades)
temperature = [45,42,25,30,35,20,12,14,15]
temp = [
    "Hot" if temperatures >= 25 else "Cold"    
    for temperatures in temperature
]
print(temp)

data = [
    [10,20],
    [30,40],
    [50,60]
]
result = []
for row in data:
    for number in row:
        result.append(number)
print(result)
result1 = [number for row in data for number in row]
print(result1)        
result2 = [number ** 2 for row in data for number in row]
print(result2)
data_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result3 = [num for row in data_1 for num in row if num %2 == 0]
print(result3)


student_marks_data = [
    [45,78,92],
    [33,67,81],
    [55,88,39]
]
flat_marks = [marks for row in student_marks_data for marks in row]
passing_marks = ["Pass" if number >= 50 else "Fail" for number in flat_marks]
passing_marks_One = [number for number in flat_marks if number >= 50]
grade = [
    "A" if mark >=90
    else "B" if mark >= 80
    else "C" if mark >= 70
    else "D" if mark >= 60
    else "Fail"
    for mark in flat_marks
]
print("Flat Marks:", flat_marks)
print("Pass/Fail:", passing_marks)
print("Passing Marks:", passing_marks_One)
print("Grade:", grade)

# Today's practice is complete.