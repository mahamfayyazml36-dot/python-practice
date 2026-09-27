# My Mini Project 6: Student Attendance Control System
# Name: Maham Fayyaz
# What it does: Takes student names and attendance (YES/NO),
#               then shows total, present, and absent students.
# What I learned: while loop, break, continue, pass, lists, counters
print("================================================================")
print("Student Attendance Control System")
print("Day 6 Mini Project")
print("================================================================")
students = []
present_students = []
absent_student = []
while True:
    name = input("Enter your student name:")
    if name == "exit":
        break
    attendance = input("Enter the present student(YES / NO):")
    if attendance == "YES":
        students.append(name)
        present_students.append(name) 
    elif attendance == "NO": 
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
print("ABSENT STUDENTS NAME:", absent_student)
print("PRESENT STUDENTS NAME:", present_students)
print("================================================================")   
print("Student Attendance System Completed")
print("================================================================") 
# Mini Project day 6 complete.
# This program takes student attendance and shows a summary.