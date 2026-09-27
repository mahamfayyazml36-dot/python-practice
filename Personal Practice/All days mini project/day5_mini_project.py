# My Mini Project 5: Food Menu Ordering System
# Name: Maham Fayyaz
# What it does: Takes food orders, calculates total, and shows final bill.
# What I learned: while loop, if-elif-else, nested if, break, accumulator

pizza = "Pizza"
burger = "Burger"
biryani = "Biryani"
exit_option = "Exit"

pizza_price = 1500
burger_price = 500
biryani_price = 200



grand_total = 0
customer_name = input("Enter your customer name:")
while True:
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
# Mini Project day 5 complete.
# This program takes food orders, validates quantity,
# calculates total, and shows final bill when customer exits. 