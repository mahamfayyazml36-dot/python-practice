# My Day 8 Python Practice
# Name: Maham Fayyaz
# What I learned today: lists (indexing, append, insert, remove, pop, len)

foods = ["Biryani", "Cake", "Apple"]

print(foods)

intro = ["Maham", 5.2, 19, True]

print(intro)

print(intro[0])
print(foods[1])
print(intro[2])
print(foods[2])


foods[1] = "cake"     # Replace
foods[0] = "Pizza"    # Replace
print(foods)


foods.append("Ice Cream")
foods.append("Burger")       # Add new item
print(foods)


foods.insert(0, "Chocolate")
foods.insert(1, "Biryani")       # Insert 
print(foods)


foods.remove("Apple")       # Remove item
print(foods)


foods.pop(0)               # Remove item by index
intro.pop()
print(foods)
print(intro)


print("Total item in list of foods:", len(foods))          # Length
print("Total item in list of intro:", len(intro))


for food in foods:               # for loop with lists
    print(food)


for food in foods:
    if food == "Biryani":
        print("Biryani available in this list of foods")    
# Today's practice is complete.
# I practiced lists: indexing, replace, append, insert,
# remove, pop, len, for loop, and if condition.