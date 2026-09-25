# ============================================================
# DAY 12 — MINI PROJECT: STUDENT DATABASE
# Topic: Dictionaries & Nested Dictionaries
# Features: View, Search, Add, Update & Delete Students
# Practiced and completed by: Maham Fayyaz
# ============================================================

students = {
    "Maham" :{
        "Age" : 19,
        "Course" : "Python",
        "City" : "Sialkot"
    },
    "Ali" :{
        "Age" : 18,
        "Course" : "AI",
        "City" : "Islamabad"
    },
    "Ayesha" : {
        "Age" : 23,
        "Course" : "MLOPs",
        "City" : "Lahore"
    }
}
print(students)
while True:
    
    print("========== STUDENT DATABASE ==========")
    print("1. View student")
    print("2. Search student")
    print("3. Add student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("View Students")
        for name, data in students.items():
            print("Name:", name)
            print("Age:", data["Age"])
            print("Course:", data["Course"])
            print("City:", data["City"])
            print("-------------------------")
    elif choice == 2:
        print("Search Student")
        name_search = input("Enter your student name:")
        if name_search in students:
            data = students[name_search]
            print("Name:", name_search)
            print("Age:", data["Age"])
            print("Course:", data["Course"])
            print("City:", data["City"])
        else:
            print("Student not found!") 
    elif choice == 3:
        print("Add Student")
        name = input("Enter student name:") 
        age = input("Enter student age:")
        course = input("Enter student course:")
        city = input("Enter student city:")
        students[name] = {
            "Age" : age,
            "Course" : course,
            "City" : city
        }   
        print("Student added successfully!")
    elif choice == 4:
        print("Update Student")
        update_name = input("Enter update student name:")
        if update_name in students:
        
            new_age = input("Enter student new age:")
            new_course = input("Enter student new course:")
            new_city = input("Enter student new city:")

            students[update_name]["Age"] = new_age
            students[update_name]["Course"] = new_course
            students[update_name]["City"] = new_city

            print("Student updated successfully!")
        else:
            print("Student not found!") 
    elif choice == 5:
        print("Delete Student")
        delete_name = input("Enter student name to delete:")
        if delete_name in students:
            students.pop(delete_name)
            print("Student delete successfully!")
        else:
            print("Student not found!")  
    elif choice == 6:
        print("Thank you for using Student Database!")
        break
    else:
        print("Invalid choice! Please select a number (1-6).")



# ============================================================
# DAY 12 MINI PROJECT COMPLETED ✅
# Practiced:
# - Dictionaries
# - Nested Dictionaries
# - Dictionary Access
# - Adding Data
# - Searching Data
# - Updating Data
# - Deleting Data
# - items()
# - pop()
# - in operator
# - while loop
# - if / elif / else
# ============================================================