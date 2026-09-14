# ============================================================
# DAY 9 — MINI PROJECT: INVENTORY MANAGER 🏪
# Topics: List Methods & Operations
# ============================================================
print("==========INVENTORY MANAGER==========")
print("1. 📦 View Inventory")
print("2. ➕ Add Product")
print("3. 📍 Insert Product")
print("4. ❌ Remove Product")
print("5. 🗑️ Remove Product by Index")
print("6. 🔄 Update Product")
print("7. 🔍 Check Product")
print("8. 🔢 Count Product")
print("9. 🔃 Sort Inventory")
print("10. ↩️ Reverse Inventory")
print("11. 🧹 Clear Inventory")
print("12. 🚪 Exit")
inventory = ["Boxing GLove", "Hand wrap", "Shin guard", "MMA Shorts"]
while True:
    choice = int(input("Enter your choice:")) 
    # 1. View Inventory
    if choice == 1:
        print("\n---View Inventory---")
        if len(inventory) == 0:
            print("Inventory is Empty")
        else:
            for number, product in enumerate(inventory, start=1):
                print(number, product)
    # 2. Add Product
    elif choice == 2:
        product = input("Enter your new product:")
        inventory.append(product)
        print("Your product added successfully append method")
        print(inventory)
    # 3. Insert product
    elif choice == 3:
        product = input("Enter your product:")
        index = int(input("Enter index number:"))
        inventory.insert(index, product)
        print("Your product added successfully with insert method")
        print(inventory)
    # 4. Remove Product
    elif choice == 4:
        product = input("Enter your product:")
        if product in inventory:
            inventory.remove(product)
            print("your product remove successfully") 
        else:
            print("product no found")
        print(inventory) 
    # 5. remove peoduct with index
    elif choice == 5:
        index = int(input("Enter your index number:"))
        if 0 <= index <len(inventory):
            inventory.pop(index)
            print("product remove with pop successfully")
        else:
            print("Invalid index")
        print(inventory) 
    # 6. Update Product
    elif choice == 6:

        index = int(input("Enter index to update: "))
        if 0 <= index < len(inventory):
            new_product = input("Enter new product name: ")
            inventory[index] = new_product
            print("Product updated successfully!")
        else:
            print("Invalid index!")

        print(inventory)
    # 7. check product

    elif choice == 7:
        product = input("Enter product to check: ")
        if product in inventory:
            print("Product is available.")
        else:
            print("Product is not available.")
        # 8. Count Product
    elif choice == 8:
        print("Total products:", len(inventory))
        product = input("Enter product to count: ")
        print(product, "appears",
              inventory.count(product),
              "time(s).")
    # 9. Sort Inventory
    elif choice == 9:
        inventory.sort()
        print("Inventory sorted successfully!")
        print(inventory)
            # 10. Reverse Inventory
    elif choice == 10:
        inventory.reverse()
        print("Inventory reversed successfully!")
        print(inventory)
            # 11. Clear Inventory
    elif choice == 11:
        inventory.clear()
        print("Inventory cleared successfully!")
        print(inventory)
            # 12. Exit
    elif choice == 12:
        print("Inventory Manager closed.")
        break
    else:
        print("Invalid choice. Please choose 1-12.")




