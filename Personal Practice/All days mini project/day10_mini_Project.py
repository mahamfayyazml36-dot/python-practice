# My Mini Project 10: Student Record System
# Name: Maham Fayyaz
# What it does: View, search, and count student records using tuples.
# What I learned: tuples, indexing, len, for loop, lower, while loop, break

print("========== STUDENT RECORD SYSTEM ==========")
students = (
    ("Leon", 18, "C++"),
    ("Nilofer", 17, "Python"),
    ("Jalan", 19, "AI"),
    ("Gohar", 20, "Data Analyst")
)
print(students)
while True:
    print("\n-----------Menu-----------")
    print("1. View Student")
    print("2. Search Student")
    print("3. Count Student")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("\n------------Student Record------------")
        for student in students:
            print("Name:", student[0])
            print("Age:", student[1])
            print("Field:", student[2])
            print("--------------------------------------")
    elif choice == 2:
        search_name = input("Enter the student name:")
        found = False
        for student in students:
            if student[0].lower() == search_name.lower():
                print("\nStudent Found")
                print("Name:", student[0])
                print("Age:", student[1])
                print("Field:", student[2])
                found = True
        if found == False:
            print("\nStudent Not Found")
            print("Please enter a name from the student record.")            
    elif choice == 3:
        print("Total Students:", len(students))
    elif choice == 4:
        print("\nThank you for using Student Record System!") 
        break  
    else:
        print("\nInvalid Choice! Please enter 1, 2, 3, or 4.") 

# Mini Project day 10 complete.
# This program is a menu-based student record system using tuples.