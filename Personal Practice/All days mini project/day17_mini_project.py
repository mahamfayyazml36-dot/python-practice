# My Mini Project 17: Delivery Cost & Logistics Utility System
# Name: Maham Fayyaz
# What it does: Calculate delivery cost, shipping charges, order total,
# discount, and delivery eligibility using Python functions.
# What I learned: functions, parameters, arguments, positional arguments,
# multiple parameters, input(), int(), float(), if-else, elif,
# while loop, break, and previous concepts.


def calculate_delivery_cost(weight, rate):
    delivery_cost = weight * rate
    print("Delivery Cost:", delivery_cost)

def shipping_cost(weight, rate):
    shipping_charges = weight * rate
    print("Shipping Charges:", shipping_charges)
   

def calculate_order_total(quantity, price):
    total_amount = quantity * price
    print("Total Amount:", total_amount)


def discount_calculator(price, discount):
    discount_amount = price * (discount / 100)
    final_amount = price - discount_amount

    print("Discount Amount:", discount_amount)
    print("Final Amount:", final_amount)


def check_delivery_eligibility(order_amount):
    if order_amount >= 5000:
        print("Amount:", order_amount)
        print("Free Delivery")
    else:
        print("Amount:", order_amount)
        print("Delivery Charges:", 250)
      
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("====================Delivery Cost & Logistics Utility System====================")
    print("1. Calculate Delivery Cost")
    print("2. Calculate Shipping Cost")
    print("3. Calculate Order Total")
    print("4. Calculate Discount")
    print("5. Check Delivery Eligibility")
    print("6. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice = input("Enter your choice (1-6):")
    if choice == "1":
        weight = float(input("Enter the Parcel Weight:"))
        rate = int(input("Enter the delivery rate pr kg:"))
        calculate_delivery_cost(weight, rate)
    elif choice == "2":
        weight = float(input("Enter the parcel weight:"))
        rate = int(input("Enter the shipping rate:"))
        shipping_cost(weight, rate)
    elif choice == "3":
        quantity = int(input("Enter the order quantity:"))
        price = int(input("Enter the product Price:"))
        calculate_order_total(quantity, price)
    elif choice == "4":
        price = int(input("Enter the order price:"))
        discount = int(input("Enter the discount:"))
        discount_calculator(price, discount)        
    elif choice == "5":
        order_amount = int(input("Enter the order amount:"))
        check_delivery_eligibility(order_amount)
    elif choice == "6":
        print("Thank you for your ordering!!")
        break
    else:
        print("Invalid your choice please select the option(1-6)")    

# Mini Project Day 17 complete.
# This program creates a Delivery Cost & Logistics Utility System
# using Python functions.
# It performs different delivery, shipping, order, and discount
# calculations based on the user's choice.
# It uses functions, parameters, arguments, arithmetic operators,
# user input, conditional statements, a while loop, and break.