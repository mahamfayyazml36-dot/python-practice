# My Day 17 Python Practice
# Name: Maham Fayyaz
# What I learned today: Parameters & Arguments (Utility Functions)
# (Parameters & Arguments Revision, Positional Arguments,
# Multiple Parameters & Arguments, Utility Functions,
# Reusing Functions, Parameters & Arguments Matching,
# Previous Concepts with Functions, and Practice Exercises)

# Topic 1: Parameters aur Arguments

def calculate_delivery(weight):
    print("Parcel Weight:", weight)
calculate_delivery(12)

def calculate_price(price):
    print("Product Price:", price)
calculate_price(2000)

def welcome_customer(customer_name):
    print("Welcome to our online store,", customer_name)
welcome_customer("Maham Fayyaz")

# Topic 2: Positional Arguments

def delivery_detail(customer, city):
    print("Customer Name:", customer)
    print("City:", city)
delivery_detail("Maham Fayyaz", "Sialkot")

def show_delivery_info(customer_name, destination_city):
    print(f"Customer Name: {customer_name}\nDestination City: {destination_city}")
show_delivery_info("Noor Salam", "Lahore")    

# Topic 3: Multiple Parameters & Arguments

def parcel_detail(customer, city, weight):
    print("Customer Name:", customer)
    print("City:", city)
    print("Weight:", weight,"Kg")
parcel_detail("Noor", "UK", 12)

def booking_details(customer, destination, parcel_count):
    print("Customer Name:", customer)
    print("Destination:", destination)
    print("Total Parcel:", parcel_count)
booking_details("Leon", "Italy", 6)

# Topic 4: Utility Functions

def calculate_delivery_cost(weight, rate):
    cost = weight * rate
    print("Delivery Cost:", cost)
calculate_delivery_cost(10, 100)
calculate_delivery_cost(12, 300)

def calculate_order_total(quantity, price):
    amount = quantity * price
    print("Total Amount:", amount)
calculate_order_total(4, 250)
calculate_order_total(3, 5000)

# Topic 5: Different Utility Functions

def calculate_delivery_cost(weight, rate):
    cost = weight * rate
    print("Delivery Cost:", cost)
def calculate_extra_charge(weight, extra_rate):
    charge = weight * extra_rate 
    print("Extra Charge:", charge)
calculate_delivery_cost(5, 600)
calculate_extra_charge(40, 1010)

def calculate_discount(price, discount):
    discount_amount = price * (discount / 100)
    one_product_price = price - discount_amount 
    print("One Product Price:", one_product_price,"rupees")
    print("Discount Amount:", discount_amount )
def calculate_shipping(weight, rate):
    cost = weight * rate
    print("Shipping Cost:", cost)
calculate_discount(25000, 100)
calculate_shipping(15, 200)

# Topic 6: Functions

def calculate_area(length, width):
    rectangle_area = length * width
    print("Area:", rectangle_area)
calculate_area(10, 5)
calculate_area(7, 3)    

# Topic 7: Arguments aur Parameters Matching

def calculate_ticket_cost(ticket_price, ticket_count):
    total_cost = ticket_price * ticket_count
    print("Total Cost:", total_cost)
calculate_ticket_cost(1200, 3)    

# Topic 8: Previous Concepts

def calculate_delivery_charges(weight):
    if weight <= 5:
        charges = weight * 100
    else:
        charges = weight * 150
    print("Delivery Charges:", charges)
calculate_delivery_charges(4)
calculate_delivery_charges(12)

def check_delivery(amount):
    if amount >= 5000:
        print("Amount:",amount)
        print("Free Delivery")
    else:
        print("Amount:", amount)
        charges = 250
        print("Delivery Charges:", charges)
check_delivery(6000)
check_delivery(3000)

# Topic 9: Practice Exercises

def calculate_electricity_bill(units, rate):
    bill_calculate = units * rate
    if bill_calculate >= 3000:
        print("High Bill")
        print("Total Bill:", bill_calculate)
    else:
        print("Normal Bill")
        print("Total Bill:", bill_calculate)
calculate_electricity_bill(40, 50)
calculate_electricity_bill(80, 50)            

# Today's practice is complete.
# I practiced parameters and arguments, positional arguments,
# multiple parameters and arguments, and utility functions.
# I also practiced reusing functions with different arguments,
# matching parameters with arguments, and combining functions
# with previous Python concepts such as variables, arithmetic
# operators, and conditional statements.
# I completed practice exercises using real-world examples.
