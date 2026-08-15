# Invoice Generator (Basic) Project
# Created by: Maham Fayyaz
# Language: Python
# Project Type: Beginner Level Mini Project
# Topics Used: Input, Variables, Type Casting, Arithmetic Operators, Calculations, f-string

print("==================================================================")
print("==================Invoice Generator (Basic)=======================")
print("==================================================================")
customer_name = input("Enter Your Customer Name:")
item_name = input("Enter Your Item Name:")
price = int(input("Enter the price of Item:"))
quantity = int(input("Enter the Quantity of Item:"))
total = price * quantity
print("===================================================================")
print("                   Invoice Generator (Basic)                       ")
print("===================================================================")
print("Customer Name:", customer_name)
print("Item Name:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print(f"Total Bill: {total}")
print("===================================================================")
print("                       THANK YOU FOR SHOPPING!                     ")
print("===================================================================")


