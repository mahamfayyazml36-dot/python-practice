# ============================================================
# DAY 9 — LIST METHODS & OPERATIONS 📋
# Topic: Python Lists
# Practiced List Methods and Operations:
# append(), insert(), remove(), pop(), clear()
# sort(), reverse(), count(), index(), copy()
# Membership Operators: in, not in
# Practiced and completed by: Maham Fayyaz
# ============================================================
# append()
foods = ["Biryani", "Pizza"]
foods.append("Burger")
print(foods)
# insert()
foods = ["Biryani", "Sajji"]
foods.insert(1,"Cold drink")
print(foods)
# remove()
favorite_subject = ["Python", "NLP"]
favorite_subject.remove("Python")
print(favorite_subject)
# pop()
introduction = [5.2, 19, "Maham Fayyaz", True]
introduction.pop()
introduction.pop(1)
print(introduction)
# clear()
ingredients = ["Flour", "Cack", "Candy"]
ingredients.clear()
print(ingredients)
# sort()
number = [50, 85, 96, 12, 45 , 23]
number.sort()
print(number)
# reverse()
course = ["Data science", "Data analyst", "Python for everybody"]
course.reverse()
print(course)
# count()
sereis = ["Abdull hamid", "ertugrul", "Mustafa kamal"]
print(sereis.count("Mustafa kamal"))

# index()
sister = ["Mafia shehzadi", "Maria", "Jannat", "Maham"]
print(sister.index("Jannat"))
# copy()
city = ["Sialkot", "UK", "Us", "Finland"]
new_citeis = city.copy()
new_citeis.append("Turkish language")
print(new_citeis)
print(city)
# in_
books =["Math", "English", "Urdu"]
print("Math" in books)
print("computer" in books)
# not in_
classes = ["Biology", "Computer", "IT"]
print("Math" not in classes)
print("Biology" not in classes)
# ============================================================
# DAY 9 COMPLETED ✅
# Practiced and understood important Python List methods,
# list operations, copying lists, and membership checking.
# ============================================================