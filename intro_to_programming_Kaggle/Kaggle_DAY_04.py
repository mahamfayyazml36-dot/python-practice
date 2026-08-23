# ============================================================
# Kaggle - Intro to Programming
# Day 4: Conditions and Conditional Statements
# Topics Covered:
# - Comparison Operators (>, <, ==, !=, <=, >=)
# - Boolean Expressions & Evaluation
# - If Statements
# - If-Else Statements
# - If-Elif-Else Chains
# - Functions with Conditional Logic
# - Real-World Kaggle Problem Solving (Grading, Pricing & Billing)
# ============================================================

#............. Startup............
print(3>5) 
print(5<10) 
print(2>3)
variable_one = 10
variable_two = 20
print(variable_one > 20)
print(variable_one <= variable_two)
print(15 == 15)        # equal to
print(15 == 13)
print(15 != 15)        # Not equal 
print(12 != 15)
print(4 < 10)           # Lessthan
print(10 < 4)
print( 15 > 20 )
print(20 > 15)           # Greaterthan
print(15 <= 16)         # Lessthan eqaul
print(15 <= 15)
print(20 >= 15)          #Greaterthan equal 
print(20 >= 20)
# if
#1
temperature = 39
if temperature >= 38:
    print("Warm sesson")
#2
age = 20
if age>= 18:
    print("You can vote")
# if else
#1
age = 15
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
#2
marks= 30
if marks >= 35:
    print("pass!")
else:
    print("Failed!")
# if elif else
mark = 850
if mark >= 900:
    print("Grade: A ")
elif mark >= 800:
    print("Grade: B ")
elif mark >= 700:
    print("Grade: C ")
else:
    print("Failed!")
#1
price = 70
if price >= 65: 
    result = price + 25
    print(result)
elif price >= 60:
    result1 = price - 25
    print(result1)
else:
    print("invalid")                   
#1
def add_five(numbers):
    if numbers < 10:
        final_result = numbers + 5
    else:
        final_result = numbers - 5
    return final_result 
print(add_five(8))
print(add_five(12))       

#2
def add_ten_or_three(number):
    if number > 15:
        result = number + 10
    else:
        result= number + 3
    return result
print(add_ten_or_three(20))
print(add_ten_or_three(10))            

#Kaggle exercise
#1

def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F" 
    return grade                  
print(get_grade(95))
print(get_grade(85)) 
print(get_grade(75))
print(get_grade(65))
print(get_grade(55))
print(get_grade(45))       

#2
def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost
print(cost_of_project("Love", True))
print(cost_of_project("Hello", False))            

#3

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        water_bill = (num_gallons/1000)*5
    elif num_gallons <= 22000:
        water_bill = (num_gallons/ 1000)*6
    elif num_gallons <= 30000:
        water_bill = (num_gallons/ 1000)*7
    else:
        water_bill = (num_gallons/ 1000)*10
    return water_bill
print(get_water_bill(7999))
print(get_water_bill(21999))
print(get_water_bill(29999))
print(get_water_bill(30002))

#4
def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        extra_gb = gb - 15
        bill = (extra_gb * 100) + 100 
    return bill
print(get_phone_bill(12))
print(get_phone_bill(15.2))         

# ============================================================
# DAY 4 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. Comparison Operators:
#    Used to compare values. Returns True or False (Boolean).
#    Operators: >, <, >=, <=, == (equal), != (not equal)

# 2. Conditional Structure:
#    - 'if': Executes code if condition is True.
#    - 'elif': Checks additional conditions if previous ones were False.
#    - 'else': Fallback code if no conditions were met.

# 3. Practical Applications Built Today:
#    - Grading System: Multi-tier logic using if-elif-else.
#    - Project Cost Estimator: Dynamic pricing based on string length & boolean conditions.
#    - Water & Phone Bill Calculators: Real-world tiered pricing and extra usage calculations.

# Status: All Kaggle Exercise 4 Questions Successfully Solved & Verified!
# ============================================================