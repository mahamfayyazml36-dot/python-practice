# My Day 20 Python Practice
# Name: Maham Fayyaz
# What I learned today: Flexible Functions — *args and **kwargs
# (*args, Multiple Positional Arguments, **kwargs,
# Keyword Arguments, Dictionary, .items(), and Mixed Practice)

def delivery_charges(*charges):
    print(charges)
delivery_charges(200,300,400,500,700)    

def all_delivery_charges_total(*charges):
    total_charges = sum(charges)
    print(total_charges)
all_delivery_charges_total(200, 300, 400, 500, 700)    

def student_result(student_name, *marks_all_subject):
    total_marks = sum(marks_all_subject)
    print(f"{student_name}, got total marks in matric {total_marks}")
student_result("Maham Fayyaz", 85, 75, 75,69,95)    

def employee_profile(**information):
    print(information)
    print(information["Education"])
    for key, value in information.items():
        print(key, ":", value)

employee_profile(name="Maham Fayyaz",
                Age=19,
                Height=5.1,
                Education="ICS",
                city="Sialkot"
            )    

def employee_id(employee_name, **details):
    print(employee_name)
    for key,value in details.items():
        print(key, ":", value)
employee_id("Noor Salam", City="Sialkot", Phone_Number="XXXXXXXXXXX")
print("~~~~~~~~~~~~~~~~~~~~~~~~*Args & **Kwargs MIxed Practice~~~~~~~~~~~~~~~~~~~~~~~~~~")
def employee_performance(employee_name, *score, **details):
    print("Employee Name:", employee_name)
    total_scores = sum(score)
    print("Total Score:", total_scores)
    for key,value in details.items():
        print(key, ":", value)
employee_performance("Usman Riaz", 45,50,60,70, phone_number="XXXXXXXXXXX", education="BSMATH")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Today's practice is complete.
# I practiced using *args and **kwargs to create
# flexible functions that can handle multiple arguments.