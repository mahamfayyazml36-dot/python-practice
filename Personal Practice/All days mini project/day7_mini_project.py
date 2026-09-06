# ================================================================
#              STUDENT GRADE & ELIGIBILITY ANALYZER
# ================================================================
# Project Type: Real-World Python Mini Project
# Python Day: Day 7 - Conditions + Loops Integration
# Created By: Maham Fayyaz
#
# Project Description:
# This project analyzes multiple students based on their age,
# marks, and attendance. It calculates each student's grade,
# checks their eligibility, counts eligible and not eligible
# students, and displays a final summary.
#
# Concepts Used:
# - Variables
# - Lists and Tuples
# - for Loop
# - if / elif / else
# - Nested / Multiple Conditions
# - and Operator
# - Comparison Operators
# - len()
# - Counting with Accumulators
# - Grade Calculation
# - Eligibility Checking
# - Multiple Students Processing
# - Data Analysis
# - Real-World Problem Solving
#
# Main Logic:
# Student Data → Grade Calculation → Eligibility Check
# → Student Result → Counting → Final Summary
# ================================================================



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
    print(name, age, marks, attendance)
    print(name, grade)
    print(name, eligibility)
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



# ================================================================
# Project Completed Successfully
#
# What I Practiced:
# I practiced processing multiple students using lists, tuples,
# for loops, conditions, comparison operators, the and operator,
# grade calculation, eligibility checking, and counting.
#
# Project Outcome:
# The program successfully calculates student grades, determines
# eligibility based on age, marks, and attendance, and displays
# the total number of eligible and not eligible students.
# ================================================================