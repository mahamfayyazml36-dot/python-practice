# Invoice Generator Project
# Created by: Maham Fayyaz
# Language: Python
# Project Type: Beginner Level Mini Project
# Topics Used: Input, Variables, Type Casting, Dictionary, 
# Calculations, Escape Sequences, sep, end, f-string, .format()


print("\n====================================================================\n")
print("=======================     INVOICE GENERATOR    ===================")
print("\n====================================================================\n")
customer_name = input("Enter Your Customer Name:")

# Item 1
item1 = {
    "product_name" : input("Enter Your first Product Name:"),
    "price" : int(input("Enter the Price of first Product:")),
    "quantity" : int(input("Enter the Quantity of first Product:"))
}
# Item 2
item2 = {
    "product_name" : input("Enter Your second Product Name:"),
    "price" : int(input("Enter the Price of second product:")),
    "quantity" : int(input("Enter the Quantity of second Product:"))
}
# Item 3
item3 ={
    "product_name" : input("Enter your third Product Name:"),
    "price" : int(input("Enter the Price of third Product:")),
    "quantity" : int(input("Enter the Quantity of third Product:"))
}
# Calculate total for each item
item1_total = item1["price"] * item1["quantity"]
item2_total = item2["price"] * item2["quantity"]
item3_total = item3["price"] * item3["quantity"]
#Total Bill
total_bill = item1_total + item2_total + item3_total
# Discount
discount = float(input("\nEnter the discount of total shopping:" ))
discount_bill = (total_bill * discount) / 100
final_total_bill = total_bill - discount_bill 

print("\n====================================================\n")
print("                    CUSTOMER INVOICE                    ")
print("========================================================")

print("CUSTOMER NAME:{}" .format(customer_name))
print("\nItem Name \tPrice \tQuantity \tTotal Bill")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(
    item1["product_name"],
    item1["price"],
    item1["quantity"],
    f"{item1_total:.2f}",
    sep ="\t"
)

print(
    item2["product_name"],
    item2["price"],
    item2["quantity"],
    f"{item2_total:.2f}",
    sep ="\t"
)

print(
    item3["product_name"],
    item3["price"],
    item3["quantity"],
    f"{item3_total:.2f}",
    sep ="\t"
)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total Bill: {:.2f}" .format(total_bill))
print("Discount: {:.2f}%".format(discount))
print("Discount Bill: {:.2f}" .format(discount_bill))
print(f"Final Bill After Discount: {final_total_bill :.2f}")

print("=========================================================")
print("                 THANK YOU For SHOPPING                  ")
print("=========================================================")