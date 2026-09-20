# ============================================================
# DAY 11 — SETS IN PYTHON
# Topic: Sets, Set Methods & Set Operations
# Practiced by: Maham Fayyaz
# ============================================================

# ============================================================
# TOPIC 1 — INTRODUCTION TO SETS
# Sets store unique values and automatically remove duplicates.
# ============================================================

participants = {"Ali", "Ahmed", "Ali", "Subhan", "Ali", "Sara", "Ahmed"}
print("Participants Student Set:", participants)

# ============================================================
# TOPIC 2 — CONVERTING LIST INTO SET
# Converting a list into a set removes duplicate values.
# ============================================================

company_name_list = ["Hatti Fight Gear", "Gel Bro","Boxing gloves","Hatti Fight Gear", "Martial art Equipment", "Boxing gloves"]
company_name_set = set(company_name_list)
print("Original List:", company_name_list)
print("Unique companies:", company_name_set)

# ============================================================
# TOPIC 3 — ADDING ITEMS TO A SET
# The add() method adds a new item to a set.
# ============================================================

products = {"Boxing gloves", "Hand wraps", "Lace up boxing gloves"}
print("Before Adding:",products)
products.add("MMA shots")
print("After Adding:", products)

# ============================================================
# TOPIC 4 — REMOVING ITEMS FROM A SET
# remove() deletes a specific item.
# discard() also deletes an item but does not raise an error
# if the item does not exist.
# ============================================================

bank = {"Habib Bank Limited", "United Bank Limited", "MCB Bank", "Meezan Bank", "Bank Alfalah", "Allied Bank", "Bank of Punjab","Askari Bank", "Faysal Bank", "National Bank of Pakistan"}
print("Before Removing:", bank)
bank.remove("MCB Bank")
bank.discard("Habib Bank Limited")
print("After removing:", bank)

# ============================================================
# TOPIC 5 — CLEARING A SET
# The clear() method removes all items from a set.
# ============================================================

chocolate_companies ={
    "Cadbury",
    "Nestlé",
    "Ferrero",
    "Lindt",
    "Galaxy"
}
print(chocolate_companies)
chocolate_companies.clear()
print(chocolate_companies)

# ============================================================
# TOPIC 6 — MEMBERSHIP: in AND not in
# in checks whether an item exists in a set.
# not in checks whether an item does not exist in a set.
# ============================================================

chocolate_companies ={
    "Cadbury",
    "Nestlé",
    "Ferrero",
    "Lindt",
    "Galaxy"
}
print("Is Cadbury available?", "Cadbury" in chocolate_companies)
print("Is Milka unavailable?", "Milka" not in chocolate_companies)

# ============================================================
# TOPIC 7 — UNION (|)
# Combines unique items from both sets.
# ============================================================

boxing_products = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
martial_art_products = {"Karate Belt", "Hand Wraps", "Shin Guards"}
all_products =boxing_products|martial_art_products
print("Boxing Product:", boxing_products)
print("Martial Art Product:", martial_art_products)
print("Combined Product:", all_products)

# ============================================================
# TOPIC 8 — INTERSECTION (&)
# Finds items that are common in both sets.
# ============================================================

boxing_products = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
martial_art_products = {"Karate Belt", "Hand Wraps", "Shin Guards"}
common_product = boxing_products & martial_art_products
print("Common Products:", common_product)

# ============================================================
# TOPIC 9 — DIFFERENCE (-)
# Finds items that exist in the first set but not in the second.
# ============================================================

boxing = {"Boxing Gloves", "Hand Wraps", "Head Guard", "Boxing Shoes"}
mma = {"MMA Gloves", "Hand Wraps", "Shin Guards", "Boxing Shoes"}
mma_only = mma - boxing
print("MMA ONLY:", mma_only)
boxing_only = boxing - mma
print("BOXING ONLY:", boxing_only)

# ============================================================
# TOPIC 10 — SYMMETRIC DIFFERENCE (^)
# Finds items that are in either set but not in both sets.
# ============================================================

boxing = {"Boxing Gloves", "Hand Wraps", "Head Guard"}
mma = {"MMA Gloves", "Hand Wraps", "Shin Guards"}
different_only = boxing ^ mma
print("Different Item:", different_only)

# ============================================================
# DAY 11 COMPLETED ✅
# Practiced Sets, Set Methods, Membership Checking,
# Union, Intersection, Difference & Symmetric Difference.
# ============================================================