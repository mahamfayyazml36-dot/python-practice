# ============================================================
# DAY 11 — MINI PROJECT: UNIQUE DATA ANALYZER
# Topic: Sets, Unique Data & Data Analysis
# Practiced by: Maham Fayyaz
# ============================================================
# This project analyzes product data using Python Sets.
# It removes duplicate products, counts unique items,
# checks product availability, and provides a simple
# interactive data analysis menu.
# ============================================================

print("========== UNIQUE DATA ANALYZER ==========")
products = [
    "Boxing Gloves",
    "Hand Wraps",
    "Boxing Gloves",
    "Shin Guards",
    "MMA Gloves",
    "Hand Wraps",
    "Boxing Gloves"
]
print("Original Products:", products)
unique_products = set(products)
print("Unique Products:", unique_products)
total_products = len(products)
total_unique_products = len(unique_products)
print("Total Original Product:", total_products)
print("Total Unique Product:", total_unique_products)
search_product = input("Enter Product name to search:")
if search_product in unique_products:
    print("Product is available")
else:
    print("product is not available")    
duplicate_count = total_products - total_unique_products
print("Duplicate Product:", duplicate_count)
while True:
    print("\n========== DATA ANALYSIS MENU ==========")
    print("1. View original Products")
    print("2. View Unique Products")
    print("3. View Total Products")    
    print("4. View Unique Product count")
    print("5. View Duplicate count")
    print("6. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Original Product:", products)
    elif choice == 2:
        print("Unique Products:", unique_products) 
    elif choice == 3:
        print("Total Products:", total_products)
    elif choice == 4:
        print("Total Unique Products:", total_unique_products)
    elif choice == 5:
        print("Duplicate Entries:", duplicate_count)
    elif choice == 6:
        print("Thank you for using Unique Data Analyzer.")
        break
    else:
        print("Invalid choice. Please select 1 to 6.")   
# ============================================================
# DAY 11 MINI PROJECT COMPLETED ✅
# Practiced:
# - Converting a List into a Set
# - Removing Duplicate Data
# - Counting Total & Unique Products
# - Checking Product Availability
# - Finding Duplicate Entries
# - Using while loop for an Interactive Menu
# - Using if, elif, else and break
# ============================================================
# Practiced and completed by: Maham Fayyaz
# ============================================================        