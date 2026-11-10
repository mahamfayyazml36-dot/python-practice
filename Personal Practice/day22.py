# My Day 22 Python Practice
# Name: Maham Fayyaz
# What I learned today: Data Processing
# (map(), filter(), reduce(), sorted(), and Lambda Functions)

number = [20, 25, 30, 10]
double_number = map(lambda number : number * 2, number)
result = list(double_number)
print(result)

addition = [20, 45, 65, 50]
add = map(lambda number : number + 2, addition)
result = list(add)
print(result)

marks = [65, 70, 80, 85]
add = map(lambda number_add : number_add + 5, marks)
result = list(add)
print(result)

names = ["maham", "ali", "Bushara"]
uppercase_names = map(lambda identity : identity.upper(), names)
result = list(uppercase_names)
print(result)

student_marks = [35, 60, 45, 50, 20, 15, 85]
passing_marks = filter(lambda number : number >= 50, student_marks)

final_result = list(passing_marks)
print(final_result)

ages = [12, 15, 16, 17, 18, 20, 22, 24, 24]
collect_ages = filter(lambda age : age >= 18, ages)
final_result = list(collect_ages)
print(final_result)


from functools import reduce
amounts = [5000, 50000, 4500, 500, 1200]
collect_amount = reduce(lambda first, second : first + second, amounts)
print(collect_amount) 

from functools import reduce
expenses = [250, 500, 300, 150, 800]
collect_expenses = reduce(lambda number_one, number_two : number_one + number_two, expenses)
print(collect_expenses)

student_marks = [75, 45, 90, 60, 85, 50]
sorted_marks = sorted(student_marks)
print(sorted_marks)

salaries = [45000, 25000, 75000, 50000, 90000, 35000]
sorted_salaries = sorted(salaries, reverse=True)
print(sorted_salaries)

students_data = [
    ("Maham", 85),
    ("MUhammad Ali", 75),
    ("Jannat", 95),
    ("Maria", 45)
]
sorted_students = sorted(students_data, key=lambda student : student[1])
print(sorted_students)

course_marks = [
    ("AI",95),
    ("ML", 45),
    ("Generative AI", 85)
]
sorted_course_marks = sorted(course_marks, key=lambda marks : marks[1], reverse=True)
print(sorted_course_marks)

# Today's practice is complete.
# I practiced Data Processing using map(), filter(), reduce(), and sorted().