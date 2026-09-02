# ================================================================
#                 FOOD MENU ORDERING SYSTEM
# ================================================================
# Project Type: Real-World Python Mini Project
# Python Day: Day 5 - While Loop
# Created By: Maham Fayyaz
#
# Project Summary:
# This project is a simple food menu ordering system created
# using Python. The program allows a customer to select food,
# enter quantity, calculate the price of each order, and maintain
# a grand total. It also validates the quantity and displays a
# final bill when the customer exits the program.
#
# Concepts Used:
# - Variables
# - input() and int()
# - while True
# - if / elif / else
# - Nested if / else
# - Comparison operators
# - break
# - Arithmetic operations
# - Accumulator / Grand Total
# - Input validation
# - Real-world problem solving
# ================================================================




grand_total = 0
customer_name =input("Enter your customer name:")
while True:
    pizza ="Pizza"
    burger = "Burger"
    biryani ="Biryani"
    exit_option = "Exit"
    pizza_price = 1500
    burger_price = 500
    biryani_price = 200
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("FOOD MENU")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.", pizza)
    print("2.", burger)
    print("3.", biryani)
    print("4.", exit_option)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("You selected Pizza")
        quantity = int(input("Enter the quantity of food:"))
        print("Quantity:", quantity)
        if quantity <= 0:
            print("Invalid Quantity")
        else:    
            print("Pizza Price:", pizza_price)
            total = pizza_price * quantity
            grand_total = grand_total + total
            print("Total Price:", total)

    elif choice == 2:
        print("You selected Burger")
        quantity = int(input("Enter the quantity of food:"))
        print("Quantity:", quantity)
        if quantity <= 0:
            print("Invalid Quantity")
        else:    
            print("Burger Price:", burger_price)
            total = burger_price * quantity
            grand_total = grand_total + total
            print("Total Price:", total)

    elif choice == 3:
        print("You selected Biryani")
        quantity = int(input("Enter the quantity of food:"))
        print("Quantity:", quantity)
        if quantity <= 0:
            print("Invalid Quantity")
        else:             
            print("Biryani Price:", biryani_price)
            total = biryani_price * quantity
            grand_total = grand_total + total
            print("Total Price:", total)
    elif choice == 4:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("FINAL BILL")
        print("Customer Name:", customer_name)
        print("Grand Total:", grand_total)
        print("Thank you for ordering.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break    
    else:
        print("Invalid user choice")            



# ================================================================
# Project Completed Successfully
#
# What I Practiced:
# I practiced building a real-world menu program using while
# loops, conditions, nested conditions, user input, validation,
# arithmetic calculations, break, and accumulator logic.
#
# Main Logic:
# Food Selection → Quantity → Validation → Price Calculation
# → Grand Total → Final Bill
#
# ================================================================        