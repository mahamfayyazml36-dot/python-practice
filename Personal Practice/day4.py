# ============================================================
# Python Practice - Day 4: for Loop
#
# Practiced and completed by: Maham Fayyaz
# This practice was completed independently while learning
# Python programming.
#
# Topics Covered:
# - Basic for Loop
# - range(stop)
# - range(start, stop)
# - range(start, stop, step)
# - Reverse range()
# - for Loop with Strings
# - for Loop with if Condition
# - Character Searching
# - Character Counting
# - for...else
# - break with for Loop
# - continue with for Loop
# - for Loop with Lists
# - for + if with Lists
# - for Loop with Tuples
# - for Loop with Dictionaries
# - Nested for Loops
# - Nested Lists with for Loops
# - enumerate() with for Loop
# - zip() with for Loop
# - Multiple Values with for Loop
# - Real-World Practice
# - AI/Data Science Related for Loop Examples
# ============================================================


# My Day 4 Python Practice


# =========== for loop ===========

# Practice 1

for number in range(1, 6):                             
    print(number) 

# Practice 2
for numbers in range(2, 21, 2):
    print(numbers)    

# Practice 3

name = "Maham Fayyaz"
for a in range(5):
    print(name)    

# =========== range() ===========

# 1️ range(stop)

print("====range 1===")
for number in range (5):
    print(number)

# 2 range(start, stop)

print("===range 2===")
for b in range(2, 8):
    print(b)

# 3 range(start, stop, step) 

print("===range 3===")  
for x in range(3, 33, 3):
    print(x)

# range Practice

# Practice 1

print("===Practice 1===")
for y in range(11):
    print(y)

# Practice 2

print("===Practice 2===")
for i in range(5, 16):
    print(i)

# Practice 3

print("===Practice 3===")
for v in range(1, 22, 2):
    print(v)

# Practice 4

print("===Practice 4===")
for u in range(10, 0, -1):
    print(u)
for ff in range(12, 1, -1):
    print(ff)
# Practice 5

print("===Practice 5===")
#number = 5
for a in range (6, 66, 6):
    print(a)         

# =========== for loop with strings ===========

# Practice 1

name = "Maham Fayyaz"
for letter in name:
    print(letter)

# Practice 2 

word = "Python"
for character in word:
    print(character)

# Practice 3

country = "Pakistan"
for city in country:
    print(city)

# Practice 4

goal = "AI"
for final_goal in goal:
    print(final_goal)    

# =========== for loop + if condition ===========

# Practice 1

word = "Python"
for letter in word:
    if letter == "o":
        print("Found o!")

# practice 2

character = "My Final Goal is AI Researcher"

for sentence in character:

    if sentence == "Z":

        print("Found Z")

    else:

        print(sentence)

# Practice 3

text = "Python Programming"

for character in text:

    if character == "P":

        print("Found P!") 

# Practice 4

names = "AI Researcher"

for vowel_word in names:

    if vowel_word in "aeiou":

        print("Found Vowel Word:", vowel_word )


# practice 5

word = "Italy"

count = 0

for character in word:

    if character == "a":

        count += 1

print("The letter a appears", count, "time.")

# ===========================================

alm = "kkkkoooppmmmkkll"

count = 0

for hhh in alm:

    if hhh in "klmjhgyuo":

        count += 1

print(f"The letter klmjhgyuo appears {count} times.")

# ===========================================

# Practice 6

sentence = "My name is Maham Fayyaz and whats your name? Broo!"

count = 0

for aquawa in sentence:

    if aquawa == "a":

        count += 1  

print("There letter a appears", count, "times.")                      

# Practice 7

name = "Maham Fayyaz"

for user_name in name:

    if user_name == "M":

        print("Found capital M ")
        
# for ... else        

# Practice 1 

print("======Practice 1 for --- else======")

for number in range(1, 6):
    print(number)

else:
    print("Completed loop!")    

# Practice 2 

print("========Practice 2 for --- else======")

name = "Maham Fayyaz"

for character in name:
    print(character)

else:
    print("completed loop!") 

# break with for

# Practice 1

print("====== Practice 1 break with for ======")

for numberss in range(1, 10):
    
    if numberss == 6:
        break
    
    print(numberss)

# Practice 2

print("====== Practice 2 break with for ======")

for number_A in range(1, 21):
    
    if number_A == 7:
        break
    
    print(number_A)

# Practice 3

print("====== Practice 3 break with for ======")
name = "Leon jaffri"

for letters in name:
    
    if letters == "a":
        break
    
    print(letters)

# continue with for

# Practice 1

print("====== Practice 1 continue with for ======")

for counting in range(1, 11):
    
    if counting == 8:
        continue
    
    print(counting)

# Practice 2

print("====== Practice 2 continue with for ======")

for count in range(1, 16, 3):
    
    if count == 7:
        continue
    
    print(count)

# Practice 3

print("====== Practice 3 continue with for ======")

names = "Sajid Imtiaz"

for nounee in names:
    
    if nounee == "I":
        continue
    
    print(nounee)

# for loop with Lists

# Practice 1

print("====== Practice 1 for loop with Lists ======")

name = ["Sajid", "Kaggle", "Python", "Programming"]

for names in name:
    print(names)

# Practice 2
print("====== Practice 1 for loop with Lists ======")

rupee = [20, 200, 300, 500, 1000, 50000]

for doller in rupee:
    print(doller)

# Practice 3

print("====== Practice 3 for loop with Lists ======")

favorite_course = ["AI", "Book", "NLP"]

for favorite in favorite_course:
    print(favorite)

# for + if with Lists

# Practice 1

print("====== Practice 1 for + if with Lists ======")

numbers = [200, 300, 400, 50000, 10000]

for number in numbers:
    
    if number %3 == 0:
        print(number) 

# Practice 2

print("====== Practice 2 for + if with Lists ======")

ages = [12, 18, 20, 22, 39, 40]

for age in ages:
    
    if age >= 22:
        print(age)

# Practice 3

print("====== Practice 3 for + if with Lists ======")

courses = ["AI", "Python", "Basics computer", "NLP", "English", "Machine Learning"]

for course in courses:
    
    if course == "NLP":
        print(course)

# for Loop with Tuples

# Practice 1

print("====== Practice 1 for Loop with Tuples ======")

courses = ("AI", "Basics computer", "NLP", "English", "Machine Learning")

for course in courses:
    print(course)

# Practice 2

print("====== Practice 2 for Loop with Tuples ======")

number_in_subject = (90, 85, 450, 500, 800, 900)

for number in number_in_subject:
    
    if number >= 500:
        print(number)

# for loop with Dictionaries
#Practice1
print("======Practice 1 for loop with Dictionaries ======")
print("====Key====")
student = {
    "name": "Maham",
    "age": 19,
    "height" : 5.2,
    "education": "ICS"

}        
for data in student:
    print(data)
#Practice 2

print("======Practice 2 for loop with Dictionaries ======")
print("===value===")
courses = {
    "course1": "AI",
    "course2": "AI Ethics",
    "course3": "NLP",
    "course4": "ML"
}
for course in courses.values():
        print(course)
# Practice 3
print("======Practice 3 for loop with Dictionaries ======")
print("====Key, value====")
customer_rupee = {
    "bag_price": 500,
    "laptop": 150000,
    "head_phone": 5000
}        
for product_name, price in customer_rupee.items():
    print(product_name, ":", price )

# Practice 4

print("====== Practice 4 Dictionary + if ======")

student = {
    "name": "Maham",
    "age": 20,
    "course": "AI",
    "country": "Pakistan"
}
for key, value in student.items():
    if key == "course":
        print(key, ":", value)

# Practice 5
        

print("====== Practice 5 Dictionary + if + break ======")
student = {
    "name": "Maham",
    "age": 20,
    "course": "AI",
    "country": "Pakistan"
}
for key, value in student.items():
    if key == "country":
        print(key, ":", value)
        break

# Practice 6
print("====== Practice 6 Dictionary + if + continue ======")

student = {
    "name": "Maham",
    "age": 20,
    "course": "AI",
    "country": "Pakistan"
}    
for key, value in student.items():
    if key == "age":
        continue
    print(key, ":", value)


# Nested for Loops

# Practice 1

print("====== Practice 1 Nested for Loop ======")

for j in range(1, 4):
    
    for k in range(1,4):
        print(j, k)

# Practice 2

print("====== Practice 2 Nested for Loop ======")

for jj in range(1, 11):
    
    for kk in range(1, 6):
        print(jj, kk)

# Practice 3

print("====== Practice 3  Nested for Loop ======")

names = ["MAHAM", "JANNAT", "MARIA", "MAFIA"]
courses =["Python", "COMPUTER BASICS", "AI", "ML"]

for name in names:
    for course in courses:
        print(name, "__", course)

# Practice 4

print("====== Practice 4 Nested for Loop ======")    

numbers = [1, 2, 3, 4, 5]
letters =["A", "B", "c", "D", "E"]

for number in numbers:
    for letter in letters:
        if number == 3:
            print(number, "=", letter)

# practice 5

print("====== Practice 5 Nested Loop + if ======")

for number in range(0, 20, 2):
    for numbers in range(11, 16):
        if numbers == 12:
            print(number, numbers)

# Practice 6

print("====== Practice 2: Nested Loop + break ======")

for i in range(1, 11):
    for j in range(1, 6):
        if j == 5:
            break
        print(i, "_", j)
# Practice 7

print("====== Practice 7: Nested Loop + continue ======")
names = ["Maham", "Jannat", "Leon"]
courses = ["AI", "ML", "NLP"]
for name in names:
    for course in courses :
        if course == "ML":
            continue
        print(name, course)

# Nested Lists 

# Practice 1

print("====== Nested Lists — Practice 1 ======")
courses = [
    ["AI", "Ml"],
    ["NLP", "MLOPs", "AI Ethics"],
    ["COMPUTER BASICS", "Deep Learning", "Cloud", "CHatgpt"]
]
for gml in courses:
    for course in gml:
        print(course)

# Practice 2

print("====== Nested Lists — Practice 2 __ if ======")

numbers = [
    [12, 13, 500, 40000],
    [1250, 12540, 156, 5653],
    [156, 13781, 345656, 24633, 43465]
]
for number in numbers:
    for count in number:
        if count == 345656:
            print(count)

# Practice 3

print("====== Nested Lists — Practice 3 __ Break ======")

shop = [
    ["bag", "cloth"],
    ["Books", "Copies", "stationary"],
    ["Laptop", "Head Phone", "Air birds", "Bike"]
]
for shopes in shop:
    for group_section in shopes:
        if group_section == "Air birds":
            break
        print(group_section)

# Practice 4

print("====== Nested Lists — Practice 4 __ continue ======")

school =[
    ["ELc", "Turabad", "Pakki Kottli"],
    ["TEACHER1", "TEACHER2", "TEACHER3", "TEACHER4"]
]
for college in school:
    for schools in college:
        if schools == "TEACHER1":
            continue
        print(schools)
# REAL WORLD PRACTICE

print("====== Real World Practice 1 ======")

shopping = [
    ["Maham", "LAPTOP", "HEAD PHONE"],
    ["ALi", "Shoes", "Jacket"]
]

for shoping in shopping:

    for data in shoping:
        if data == "Shoes":
            break
        print(data) 

# enumerate() with for
#Practice 1
print("====== Practice 1 enumerate() with for ======")

course = ["AI", "ML", "DL", "Cloude", "NLP"]
for index, courses in enumerate(course):
    print(index, courses)

# Practice 2
print("====== Practice 2 enumerate() with for ======")

name = ["Maham", "Muhammad Ali", "Maria", "Mafia", "Jannat", "Noor Salam", "Muhamma Fiaz", "Shameem Fiaz"]
for index, names in enumerate(name, start=1):

    print(index, names)
# Practice 3 enumerate() + if
students = ["Maham", "Ali", "Sara", "Ahmed"]

for number, student in enumerate(students, start=1):
    if student == "Sara":
        print("Sara is at position:", number)
# Practice 4 enumerate() + if/else
marks =[80, 85, 95, 42]
for numbers, mark in enumerate(marks, start=1):
    if mark >= 60:
        print(numbers, mark, "Pass!")
    else:
        print(numbers, mark, "fail!")                
# Practice 5 enumerate() + nested list
shopping = [
    ["Maham", "Laptop", "Headphones"],
    ["Ali", "Shoes", "Jacket"],
    ["Sara", "Bag", "Watch"]
]

for number, person in enumerate(shopping, start=1):
    print(number, person)

# Practice 6 enumerate() + nested list +value find
shopping = [
    ["Maham", "Laptop", "Headphones"],
    ["Ali", "Shoes", "Jacket"],
    ["Sara", "Bag", "Watch"]
]

for number, person in enumerate(shopping, start=1):
    
    print("Customer:", number)

    for item in person:
        print(item)   
# Practice 7 enumerate() + string        

name = "Maham"

for position, letter in enumerate(name, start=1):
    print(position, letter)

# Practice 8 enumerate() + break
students = ["Maham", "Ali", "Sara", "Ahmed"]

for number, student in enumerate(students, start=1):

    if student == "Sara":
        print("Found at:", number)
        break

    print(student)

# Practice 9 enumerate() + continue
students = ["Maham", "Ali", "Sara", "Ahmed"]

for number, student in enumerate(students, start=1):

    if student == "Sara":
        continue

    print(number, student)        


# Practice final check 
products = ["Laptop", "Mouse", "Keyboard", "Headphones"]

prices = [80000, 2000, 3500, 5000]
for index, price in enumerate(prices, start=1):
    product = products[index - 1]

    print(index, product, price)
# Practice 1
products = ["Laptop", "Mouse", "Keyboard", "Headphones"]

prices = [80000, 2000, 3500, 5000]
for number, product in enumerate(products, start = 1):
    price = prices[number - 1]
    if price <= 3000:
        print(number, product, price, "Low cost of product!")
    else:
        print(number, product, price, "High cost of product!")    

# zip() with for
students = ["Maham", "Ali", "Sara", "Ahmed"]

marks = [85, 42, 76, 35]
for student, mark in zip(students, marks):
    print(student, mark)

# Practice 1
students = ["Maham", "Ali", "Sara", "Ahmed"]

marks = [85, 42, 76, 35]
books= ["math", "Economics", "computer"]
for student, mark, book in zip(students, marks, books):
    if mark >= 60:
        print(student, mark, book, "Pass")
    else:
        print(student, mark, book, "Fail!")
        


# ============================================================
# DAY 4 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. Basic for Loop:
#    - Learned how to repeat a block of code using a for loop.
#
# 2. range():
#    - Practiced range(stop).
#    - Practiced range(start, stop).
#    - Practiced range(start, stop, step).
#    - Practiced reverse ranges using a negative step.
#
# 3. for Loop with Strings:
#    - Learned how to iterate through characters in a string.
#
# 4. for Loop with if:
#    - Practiced checking conditions while looping.
#    - Used loops for character searching and counting.
#
# 5. for...else:
#    - Practiced using else with a for loop.
#
# 6. break:
#    - Practiced stopping a for loop when a specific condition
#      becomes True.
#
# 7. continue:
#    - Practiced skipping the current iteration and continuing
#      with the next iteration.
#
# 8. for Loop with Lists:
#    - Practiced iterating through list elements.
#    - Combined for loops with if conditions.
#
# 9. for Loop with Tuples:
#    - Practiced iterating through tuple elements.
#
# 10. for Loop with Dictionaries:
#     - Practiced accessing dictionary keys.
#     - Practiced accessing dictionary values using values().
#     - Practiced accessing keys and values using items().
#
# 11. Nested for Loops:
#     - Practiced using one for loop inside another for loop.
#
# 12. Nested Lists:
#     - Practiced iterating through lists containing other lists.
#
# 13. enumerate():
#     - Practiced getting both index and value while looping.
#     - Used enumerate() with lists, strings and nested lists.
#
# 14. zip():
#     - Practiced looping through multiple collections together.
#
# 15. Real-World Practice:
#     - Applied for loops to shopping, products, students,
#       courses and other practical examples.
#
# 16. AI/Data Science Practice:
#     - Practiced loop-based conditions using examples related
#       to AI, ML and data-oriented situations.
#
# Status: Day 4 for Loop Practice Completed Successfully!
# ============================================================