# 📚 DAY 12 — STUDENT DATABASE

## 🐍 Python Dictionaries & Nested Dictionaries

This is my **Day 12 Python mini project**, created to practice dictionaries and nested dictionaries.

The project is a simple **Student Database System** where student information can be viewed, searched, added, updated, and deleted.

---

## 🎯 Project Objective

The main purpose of this project is to practice:

* Dictionaries
* Nested Dictionaries
* Dictionary access
* Adding dictionary data
* Updating dictionary data
* Deleting dictionary data
* `items()`
* `pop()`
* `in` operator
* `while` loop
* `if / elif / else`
* User input

---

## 🗂️ Student Information

Each student has the following information:

* Name
* Age
* Course
* City

Example:

```python
students = {
    "Maham": {
        "Age": 19,
        "Course": "Python",
        "City": "Sialkot"
    }
}
```

---

## ⚙️ Features

### 1. View Students

Displays all students and their information.

### 2. Search Student

Searches for a student by name.

### 3. Add Student

Allows the user to add a new student with:

* Name
* Age
* Course
* City

### 4. Update Student

Allows the user to update an existing student's information.

### 5. Delete Student

Removes a student from the database.

### 6. Exit

Closes the Student Database program.

---

## 🧠 What I Practiced

Through this project, I practiced working with **nested dictionaries** and learned how to access and modify data inside them.

For example:

```python
students["Maham"]["Age"]
```

I also practiced adding and updating data:

```python
students[name] = {
    "Age": age,
    "Course": course,
    "City": city
}
```

And deleting a student:

```python
students.pop(delete_name)
```

---

## 🛠️ Technologies Used

* Python
* Visual Studio Code

---

## 📁 Project File

```text
Day 12/
│
├── student_database.py
└── README.md
```

---

## 👩‍💻 Author

**Maham Fayyaz**

Python Learner | Aspiring AI Engineer

---

## ✅ Project Status

**Completed**

This project is part of my ongoing Python learning journey.
