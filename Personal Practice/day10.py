# My Day 10 Python Practice
# Name: Maham Fayyaz
# What I learned today: tuples 
# (indexing, slicing, unpacking, count, index, len, in, not in, +, 
# *, nested tuples)
student = ("Maham", 19, 5.2, "AI")
print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])
field = ("AI", "NLP", "MLOps", "Java")
print(field[-1])
print(field[-2])
print(field[-3])
print(field[-4])
food = ("Biryani", "Shawarma", "Pizza", "Kurma", "Salad")
print(food[0:2])
print(food[0:3])
print(food[:4])
print(food[3:])

introduction = ("Maham Fayyaz", 20, 5.1, "NLP")
name, age, height, language = introduction
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Language:", language)
print("My name is", name, ". I am", age, "years old. My height is", height, "and I learn the language of", language,".")
language = ("Java", "MLOps", "NLP", "MLOps", "C++", "C#", "c", "Python", "c", "c")
print(language.count("c"))
print(language.count("Java"))
print(language.index("c"))
number = (10, 20, 30, 40, 10, 10, 30, 30)
print(number.count(10))
print(number.count(30))
print(number.index(30))

intro = ("Maham", "Jannat", "Maria", "Mafia")
print(intro)
# intro[2] = "Ayesha"
# print(intro)
business = ("Gel Bro", "Hatti Fight Gear", "UFC")
print(len(business))
print(business)
print("UFC" in business)
print("Nike" not in business)
first = ("NLP", "MLOps", "Java")
second = ("Python", "Data Analyst", "Data Science")
subject = first + second
print(subject)
number = (5, 6, 7)
result = number * 2
print(result)
numbers = 6
for a in range(1, 11):
    print(numbers, "x", a, "=", numbers * a)
computer = (
    ("Dell", "HP", "Lenovo", "Acer"),
    ("Asus", "Apple", "Samsung"),
    ("Toshiba", "Microsoft Surface", "MSI")
)
print(computer)
print(computer[0])
print(computer[0][0])
print(computer[1][2])
print(computer[2][0])    

# Today's practice is complete.
# I practiced tuples: indexing, slicing, unpacking, count, index,
# len, in, not in, concatenation (+), repetition (*), and nested tuples.