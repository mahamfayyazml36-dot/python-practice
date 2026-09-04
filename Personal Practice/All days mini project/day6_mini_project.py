# ================================================================
# Student Attendance Control System
# Day 6 Mini Project
# ================================================================
# Project Description:
# A beginner-level Python project for managing student attendance.
# This project practices while loops, break, continue, pass,
# conditions, lists, user input, validation, and counting.
# ================================================================

print("================================================================")
print("Student Attendance Control System")
print("Day 6 Mini Project")
print("================================================================")
students =[]
present_students = []
total_students = 0
absent_student = []
while True:
    name = input("Enter your student name:")
    if name == "exit":
        break
    attendance = input("Enter the present student(YES / NO):")
    if attendance == "YES":
        students.append(name)
        present_students.append(name) 
    elif attendance =="NO": 
        students.append(name)
        absent_student.append(name)
        pass
    else:
        print("Invalid attendance! please enter YES or NO")
        continue
    total_students = len(students)
print("================================================================")   
print("Attendance Summary") 
print("================================================================")   
print("TOTAL STUDENTS:", total_students)
print("PRESENT STUDENTS:", len(present_students))
print("ABSENT STUDENTS:", len(absent_student))
print("ABSENT STUDENTS:", absent_student)
print("PRESENT STUDENTS NAME:", present_students)
print("================================================================")   
print("Student Attendance System Completed")
print("================================================================") 

# ================================================================
# Project Completed
# Concepts Practiced:
# while loop, break, continue, pass, if/elif/else,
# lists, append(), len(), input validation, and counters.
# ================================================================