# ============================================================
# DAY 10 — MINI PROJECT: STUDENT RECORD SYSTEM 🎓
# Topic: Tuples
# Concepts Practiced:
# Tuple Creation, Indexing, len(), for Loop
# Tuple Searching, lower(), Boolean Values (True/False)
# while Loop, if-elif-else, break
# Membership and Tuple-Based Student Records
# Practiced and completed by: Maham Fayyaz
# ============================================================

print("========== STUDENT RECORD SYSTEM ==========")
students = (
    ("Leon", 18, "C++"),
    ("Nilofer", 17, "Python"),
    ("Jalan", 19, "AI"),
    ("Gohar", 20, "Data analyst")
)
print(students)
while True:
    print("\n-----------Menu-----------")
    print("1. View Student")
    print("2. Search Student")
    print("3. Count student")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("\n------------Student Rcord------------")
        for student in students:
            print("Name:", student[0])
            print("Age:", student[1])
            print("Feild:", student[2])
            print("--------------------------------------")
    elif choice == 2:
        search_name = input("Enter the student name:")
        found =False
        for student in students:
            if student[0].lower() == search_name.lower():
                print("\nStudent Found✅")
                print("Name:", student[0])
                print("Age:", student[1])
                print("Feild:", student[2])
                found = True
        if found == False:
            print("\nStudent Not Found ❌")
            print("Please enter a name from the student record.")            
    elif choice == 3:
        print("Total Students:", len(students))
    elif choice == 4:
        print("\nThank you for using Student Record System! 👋") 
        break  
    else:
        print("\nInvalid Choice ❌ Please enter 1, 2, 3, or 4.") 


# ============================================================
# DAY 10 MINI PROJECT COMPLETED ✅
# Built an interactive Student Record System using Python Tuples.
# Practiced viewing student records, searching students,
# counting students, handling invalid choices, and exiting
# the program using a while loop and break.
# ============================================================