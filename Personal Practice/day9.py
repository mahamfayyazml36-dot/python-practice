# My Day 9 Python Practice
# Name: Maham Fayyaz
# What I learned today: list methods 
# (append, insert, remove, pop, clear, sort, reverse, count, index, copy)

# append()
foods = ["Biryani", "Pizza"]
foods.append("Burger")
print(foods)
# insert()
foods = ["Biryani", "Sajji"]
foods.insert(1, "Cold drink")
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
ingredients = ["Flour", "Cake", "Candy"]
ingredients.clear()
print(ingredients)
# sort()
number = [50, 85, 96, 12, 45, 23]
number.sort()
print(number)
# reverse()
course = ["Data science", "Data analyst", "Python for everybody"]
course.reverse()
print(course)
# count()
series = ["Abdul Hamid", "Ertugrul", "Mustafa Kamal"]
print(series.count("Mustafa Kamal"))

# index()
sister = ["Mafia Shehzadi", "Maria", "Jannat", "Maham"]
print(sister.index("Jannat"))
# copy()
city = ["Sialkot", "UK", "US", "Finland"]
new_cities = city.copy()
new_cities.append("Turkish Language")
print(new_cities)
print(city)
# in
books = ["Math", "English", "Urdu"]
print("Math" in books)
print("computer" in books)
# not in
classes = ["Biology", "Computer", "IT"]
print("Math" not in classes)
print("Biology" not in classes)
# Today's practice is complete.
# I practiced list methods, list operations, copying lists,
# and membership checking (in, not in).