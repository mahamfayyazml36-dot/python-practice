# My Mini Project 7: Student Grade & Eligibility Analyzer
# Name: Maham Fayyaz
# What it does: Calculates grades and eligibility for multiple students
# based on age, marks, and attendance.
# What I learned: for loop, if-elif-else, and operator, accumulators, tuples



print("================================================================")
print("Student Grade & Eligibility Analyzer")
print("Day 7 Mini Project")
print("================================================================")
students = [
    ("Ali", 25, 85, 80),
    ("Sara", 24, 80, 78),
    ("Maham", 20, 92, 95),
    ("Ahmed", 22, 45, 90),
    ("Ayesha", 19, 65, 60)
]
eligible_count = 0
not_eligible_count = 0
for name, age, marks, attendance in students:
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D" 
    else:
        grade = "Fail"  
    if age >= 18 and marks >= 50 and attendance >= 75:
        eligibility = "Eligible"
        eligible_count = eligible_count + 1
    else:
        eligibility = "Not Eligible"      
        not_eligible_count = not_eligible_count + 1               
    print("--------------------------------")
    print("Student:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Attendance:", attendance)
    print("Grade:", grade)
    print("Eligibility:", eligibility)
print("================================================================")
print("FINAL SUMMARY")
print("================================================================")
print("Total Students:", len(students))
print("Eligible Students:", eligible_count)
print("Not Eligible Students:", not_eligible_count)
print("================================================================")
print("Student Grade & Eligibility Analyzer Completed")
print("================================================================")
# Mini Project day 7 complete.
# This program calculates grades and eligibility for multiple students.