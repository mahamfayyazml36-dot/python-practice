# Day 29 Mini Project
# Student Performance Generator

# Student Data
# Student Generator
# High Marks Generator
# Total Marks
# Average Marks
# Highest Marks
# Batch Generator

students = [
    {"name": "Ali", "marks": 80},
    {"name": "Sara", "marks": 90},
    {"name": "Ahmed", "marks": 65},
    {"name": "Maham", "marks": 95},
    {"name": "Ayesha", "marks": 72}
]
def student_data():
    for student in students:
        yield student
for student in student_data():
    print(student)
def high_marks():
    for student in students:
        if student["marks"] >= 80:
            yield student
for marks in high_marks():
    print(marks)
total_marks = 0
for student in students:
    total_marks += student["marks"]
print("Total Marks:",total_marks)
count = 0
for student in students:
    count += 1
    average = total_marks/count
print("Average:", average)
highest = 0
for student in students:
    if student["marks"] > highest:
        highest = student["marks"]
print("Highets Marks:", highest)
def batch_generator():
    for student in range(3):
        batch = [student * 5 + j for j in range(5)]             
        yield batch
for number in batch_generator():
    print(number)        

# Today's Day 29 mini project is complete.