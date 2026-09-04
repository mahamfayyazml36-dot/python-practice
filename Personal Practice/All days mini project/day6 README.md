# Student Attendance Control System

## 📌 Project Overview

The **Student Attendance Control System** is a beginner-level Python mini project created as part of **Day 6 Python Practice**.

The project allows the user to enter student names and mark their attendance as **YES** or **NO**. At the end, it displays the total number of students, present students, absent students, and their names.

## 🎯 Project Purpose

The main purpose of this project is to practice Python control-flow statements and apply them to a simple real-world problem.

## 🛠️ Concepts Used

* `while True`
* `break`
* `continue`
* `pass`
* `if / elif / else`
* Lists
* `.append()`
* `len()`
* User input
* Input validation
* Counters
* Basic problem-solving logic

## ⚙️ How It Works

1. The program asks the user to enter a student name.
2. If the user enters `exit`, the program stops.
3. The program asks whether the student is present using `YES` or `NO`.
4. If the attendance is `YES`, the student is added to the present students list.
5. If the attendance is `NO`, the student is added to the absent students list.
6. Invalid attendance input is rejected using `continue`.
7. The program calculates the total number of students.
8. Finally, an attendance summary is displayed.

## 💻 Example Output

```text
Student Attendance Control System
Day 6 Mini Project

Enter your student name: Maham
Enter the present student(YES / NO): YES

Enter your student name: Sara
Enter the present student(YES / NO): NO

Enter your student name: Ali
Enter the present student(YES / NO): YES

Enter your student name: exit

Attendance Summary

TOTAL STUDENTS: 3
PRESENT STUDENTS: 2
ABSENT STUDENTS: 1
ABSENT STUDENTS: ['Sara']
PRESENT STUDENTS NAME: ['Maham', 'Ali']

Student Attendance System Completed
```

## 📚 What I Practiced

Through this project, I practiced how `break`, `continue`, and `pass` work with a `while` loop and conditional statements.

I also practiced using lists to store student information and using `.append()` and `len()` to add and count data.

## 👩‍💻 Project By

**Maham Fayyaz**

## 🐍 Learning Stage

**Python — Day 6 Mini Project**
