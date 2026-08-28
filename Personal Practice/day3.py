# ============================================================
# Python Practice - Day 3: Conditional Statements
#
# Practiced and completed by: Maham Fayyaz
# This practice was completed independently while learning
# Python programming.
#
# Topics Covered:
# - if Statement
# - if-else Statement
# - if-elif-else Statement
# - Nested if Statements
# - Nested if-else Statements
# - Nested if-elif-else Statements
# - Logical Operators with if
# - Using and, or and not with Conditions
# - Building Conditions for Real-World Examples
# ============================================================

# My Day 3 Python Practice


# if statement
age = 20
if age >= 18:
    print("your are adult!")

height = 5.2
if height <= 5.6:
    print("Nice your height!") 

age = 45
if age >= 40:
    print("Great!")

#if else statement
#1.
age = 16
if age >= 18:
    print("you can vote.") 
else:
    print("You can not vote!") 
#2.
marks = 850
if marks >= 750:
    print("you are intelligent student.")
else:
    print("normal marks")  
#3.
temperature = 52
if temperature >= 40:
    print("Today is hot!")
else:
    print("Today is cold!")  


# if elif else statement
marks = 85
if marks >= 90:
    print("Your grade: A")
elif marks >= 80:
    print("Your grade: B") 
elif marks >= 70:
    print("your grade: C")
else:
    print("You are fail!!!!")        

# Nested if
#1.
age = 25
voter = True
if age >= 18:
    if voter:
        print("you can enter in pak militry acadamy.")
#2.
temperature = 30
season_cold = True
if temperature <= 42:
    if season_cold:
        print("Today season is nice!")
#3.
marks = 85
attendence = 80
if marks >= 80:
    if attendence >= 50:
        print("Your progress is Excellent!") 
#4. 
ice = 50
rain = True               
if ice >= 12:
    if rain:
        print("Please you can go in home.")

# Nested if else
#1.
age = 18
voter = False
if age >= 18:
    if voter:
        print("You can  adult for voting like noonleague or tehrike-insaf")
    else:
        print("You need National Indentity Card" )
else:
    print("You are under 18.")
#2.
marks = 70
atendence = 80
if marks >= 50:
    if atendence >= 75:
        print ("you passed!")
    else:
        print("Your atendence is too low!") 
else:
    print("you failed")

#3.
weather = 20
rainy = False
if weather >= 20:
    if rainy:
        print("Weather is warm but rainy.")
    else:
        print("Weather is warm but cleaner.")                   
else:
    print("weather is too much cold.")
#Nested if elif else
#1.
model_prediction = "positive"
confidence = 0.86
if model_prediction == "positive":
    if confidence >= 0.90:
        print("Your model is too much high confidence")
    elif confidence >= 0.70:
        print("Medium confidence")
    else:
        print("Low confidence") 
else:
    print("Negative prediction your model") 
#2. 
price = 300000
if price >= 200000:
    if price >=500000:
        print("house is not afordable!")
    elif price >= 280000:
        print("Midum price house it's afordable!")
    else:
        print("cheap price house!")
else:
    print("Price is too low!") 

#🐍 Logical Operators with if
#1. and (dunu condition true huni chahiye)
model_accuracy = 92
model_ready = True
if model_accuracy >= 90 and model_ready: 
    print("Your model is ready for deployment!")
else:
    print("mdel need more work!") 
# 2. or (kam az kam aik condition True honi chahiye)
accuracy = 75
f1_score = 90
if accuracy >= 90 or f1_score >=85:
    print("Matrix condition good!")
else:
    print("Need more wor on model!") 
#3. not 
modelfailed = False
if not modelfailed:
    print("Model is good working!") 
else:
    print("Model is hectic")          
       

# ============================================================
# DAY 3 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. if Statement:
#    - Learned how to execute code when a condition is True.
#
# 2. if-else Statement:
#    - Learned how to execute different code depending on
#      whether a condition is True or False.
#
# 3. if-elif-else Statement:
#    - Practiced checking multiple conditions.
#    - Used it to create a simple grading system.
#
# 4. Nested if:
#    - Learned how to place one if statement inside another
#      if statement.
#
# 5. Nested if-else:
#    - Practiced multiple conditions using nested if and else
#      statements.
#
# 6. Nested if-elif-else:
#    - Practiced more complex decision-making using nested
#      conditions.
#
# 7. Logical Operators with if:
#    - Practiced 'and', 'or' and 'not' with conditional
#      statements.
#    - Used conditions with AI/ML examples such as model
#      accuracy, confidence and deployment readiness.
#
# 8. Practical Practice:
#    - Created different decision-making programs using
#      real-world examples such as age, marks, weather,
#      prices and AI model predictions.
#
# Status: Day 3 Conditional Statements Practice Completed Successfully!
# ============================================================       