# My Mini Project 11: Unique Data Analyzer
# Name: Maham Fayyaz
# What it does: Removes duplicates, counts unique items, and checks availability.
# What I learned: sets, set(), len, in, while loop, if-elif-else, break

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
print("Total Original Products:", total_products)
print("Total Unique Product:", total_unique_products)
search_product = input("Enter Product name to search:")
if search_product in unique_products:
    print("Product is available")
else:
    print("Product is not available")    
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
# Mini Project day 11 complete.
# This program analyzes product data using sets to remove duplicates.   