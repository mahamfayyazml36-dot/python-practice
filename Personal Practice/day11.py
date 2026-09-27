# My Day 11 Python Practice
# Name: Maham Fayyaz
# What I learned today: sets 
# (add, remove, discard, clear, in, not in, union, intersection,
#  difference, symmetric difference)

# 1. Introduction to sets (unique values, remove duplicates)

participants = {"Ali", "Ahmed", "Ali", "Subhan", "Ali", "Sara", "Ahmed"}
print("Participants Student Set:", participants)

# 2. Converting list into set

company_name_list = ["Hatti Fight Gear", "Gel Bro", "Boxing Gloves","Hatti Fight Gear", "Martial Art Equipment", "Boxing Gloves"]
company_name_set = set(company_name_list)
print("Original List:", company_name_list)
print("Unique companies:", company_name_set)

# 3. Adding items to a set (add)

products = {"Boxing Gloves", "Hand Wraps", "Lace Up Boxing Gloves"}
print("Before Adding:", products)
products.add("MMA Shorts")
print("After Adding:", products)

# 4. Removing items from a set (remove, discard)

bank = {"Habib Bank Limited", "United Bank Limited", "MCB Bank", "Meezan Bank", "Bank Alfalah", "Allied Bank", "Bank of Punjab","Askari Bank", "Faysal Bank", "National Bank of Pakistan"}
print("Before Removing:", bank)
bank.remove("MCB Bank")
bank.discard("Habib Bank Limited")
print("After removing:", bank)

# 5. Clearing a set (clear)

chocolate_companies = {
    "Cadbury",
    "Nestlé",
    "Ferrero",
    "Lindt",
    "Galaxy"
}
print(chocolate_companies)
chocolate_companies.clear()
print(chocolate_companies)

# 6. Membership: in and not in

chocolate_companies = {
    "Cadbury",
    "Nestlé",
    "Ferrero",
    "Lindt",
    "Galaxy"
}
print("Is Cadbury available?", "Cadbury" in chocolate_companies)
print("Is Milka unavailable?", "Milka" not in chocolate_companies)

# 7. Union (|) - combines unique items from both sets

boxing_products = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
martial_art_products = {"Karate Belt", "Hand Wraps", "Shin Guards"}
all_products = boxing_products | martial_art_products
print("Boxing Products:", boxing_products)
print("Martial Art Products:", martial_art_products)
print("Combined Products:", all_products)

# 8. Intersection (&) - finds common items in both sets

boxing_products = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
martial_art_products = {"Karate Belt", "Hand Wraps", "Shin Guards"}
common_product = boxing_products & martial_art_products
print("Common Products:", common_product)

# 9. Difference (-) - items in first set but not in second

boxing = {"Boxing Gloves", "Hand Wraps", "Head Guard", "Boxing Shoes"}
mma = {"MMA Gloves", "Hand Wraps", "Shin Guards", "Boxing Shoes"}
mma_only = mma - boxing
print("MMA ONLY:", mma_only)
boxing_only = boxing - mma
print("BOXING ONLY:", boxing_only)

# 10. Symmetric difference (^) - items in either set but not both

boxing = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
mma = {"MMA Gloves", "Hand Wraps", "Shin Guards"}
different_only = boxing ^ mma
print("Different Items:", different_only)

# Today's practice is complete.
# I practiced sets: add, remove, discard, clear, in, not in,
# union, intersection, difference, and symmetric difference.