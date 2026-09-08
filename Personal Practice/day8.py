# ============================================================
# DAY 8 — PYTHON LISTS PRACTICE
# Topics: List, Indexing, Replace, append, insert,
# remove, pop, len, for loop, if condition
# ============================================================

foods = ["BIryani", "Cack", "Apple"]

print(foods)

intro = ["Maham", 5.2, 19, True]

print(intro)

print(intro[0])
print(foods[1])
print(intro[2])
print(foods[2])


foods[1]="cake"     #REPLACE
foods[0]="Pizza"    # REPLACE
print(foods)


foods.append("Ice-Cream")
foods.append("Burger")       # ADD NEW ITEM
print(foods)


foods.insert(0, "Chocolate")
foods.insert(1,"Biryani")       # Insert 
print(foods)


foods.remove("Apple")       # REMOVE ITEM
print(foods)


foods.pop(0)               # REMOVE ITEM BUT INDEX THROUGH
intro.pop()
print(foods)
print(intro)


print("Tota item in list of foods:",len(foods))          # length
print("Total item in list of intro:",len(intro))


for food in foods:               # FOR LOOP WITH LIST
    print(food)


for food in foods:
    if food == "Biryani":
        print("Biryani available in this list of foods")    


# ============================================================
# DAY 8 — LISTS PRACTICE COMPLETED ✅
# Next: MINI PROJECT — SHOPPING LIST PROGRAM 🛒
# ============================================================        