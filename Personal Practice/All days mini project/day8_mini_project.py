# ============================================================
# DAY 8 — MINI PROJECT: SHOPPING LIST MANAGEMENT PROGRAM 🛒
# Project Features:
# 1. Add Items
# 2. Insert Item at a Specific Index 
# 3. View Shopping List
# 4. Check Item Availability
# 5. Remove Item
# 6. Remove Item by Index 
# 7. Update Item 
# 8. Count Total Items
# 9. Exit Program 
# ============================================================

print("========== SHOPPING LIST PROGRAM ==========")
print("1. Add Item")
print("2. Insert Item")
print("3. View Shopping List")
print("4. Check Item")
print("5. Remove Item")
print("6. Remove Item by Index")
print("7. Update Item")
print("8. Count Items")
print("9. Exit")

shopping_list = []
while True:

    choice = int(input("Enter your choice:"))

    if choice == 1:
        first_item = input("Enter your First Item:")
        second_item = input("Enter your Second Item:")
        third_item = input("Enter your Third Item:")

        shopping_list.append(first_item)
        shopping_list.append(second_item)
        shopping_list.append(third_item)

        print("Items added successfully!") 
        print(shopping_list)
    elif choice == 2:

        new_item = input("Enter your new item:") 
        position = int(input("Enter Position/ Index:"))
    
        shopping_list.insert(position, new_item)

        print(shopping_list)  

    elif choice == 3:
        for number,shopping in enumerate(shopping_list, start=1):
            print("Your Shopping List:",number,shopping)

    elif choice == 4:
        
        item_to_check = input("Enter item to check:")
        if item_to_check in shopping_list:
            print("Item is available")
        else:
            print("Item is not available")
    
    elif choice == 5:

        item_to_remove = input("Enter item to remove: ")

        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print("Successfully remove Item")
        else:
            print("Item not found in shopping list")

        print(shopping_list)

    elif choice == 6:

        remove_index = int(input("Enter index to remove Item:"))

        shopping_list.pop(remove_index)

        print(shopping_list)

    elif choice == 7:

        update_index = int(input("Enter index to update:"))
        update_item = input("Enter the update item:")

        shopping_list[update_index] = update_item

        print(shopping_list)

    elif choice == 8:

        print("Shopping Item:", len(shopping_list))

    elif choice == 9:    

        print("Program Exited.")
        break
# ============================================================
# DAY 8 — SHOPPING LIST PROJECT COMPLETED ✅
#
# I practiced and integrated Python Lists with Conditions
# and Loops to build a complete menu-based mini project.
#
# Day 8 Completed Successfully! 🎯🐍
# ============================================================    