# My Day 26 Python Mini Project
# Name: Maham Fayyaz
# Project: Student Marks Data Transformation
# What I practiced today: List Comprehension & Data Transformation
# (Filtering, Conditions, Nested Lists, Grade Classification, and zip())

students= [
    {"name" : "Ali", "marks" : 95},
    {"name": "Maham", "marks" : 33},
    {"name" : "Maria", "marks" :88},
    {"name": "Jannat", "marks": 67},
    {"name": "Ahmed", "marks": 81}
]
name = [student["name"] for student in students]
marks = [student["marks"] for student in students]
status = [
    "Pass" if mark >= 50 else "Fail"
    for mark in marks
    ]
grade = [
    "A" if mark >=90
    else "B" if mark >= 80
    else "C" if mark >= 70
    else "D" if mark >= 50
    else "Fail"
    for mark in marks
]
print("Name", name)
print("Student Marks:", marks)
print("Status:", status)
print("Grade:", grade)

final_data = [
    {
        "Name" : student_name,
        "Marks" : student_marks,
        "Status" : student_status,
        "Grade" : student_grade
    }
    for student_name,student_marks,student_status,student_grade in zip(name,marks,status,grade)
]
print(final_data)

# Today's practice is complete.
# Day 26 completed successfully!