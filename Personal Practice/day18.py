# My Day 18 Python Practice
# Name: Maham Fayyaz
# What I learned today: Return in Python Functions
# (Return Statement, Returning Different Types of Values,
# Storing Returned Values, Using Returned Values Again,
# Returning Different Values Based on Conditions,
# Returning Multiple Values from a Function,
# and Combining Return with Previous Python Concepts)

# Topic 1: return in Python Functions
def add(a, b):
    return a + b
result = add(15, 20)
print(result)

def calculate():
    return 200
    print("Hello! How are you?")
result = calculate()
print(result)

def calculate_price(price, quantity):
    return price * quantity
total_price = calculate_price(200, 4)
print(total_price)

# Topic 2: Returning Different Types of Values

def get_city():
    return "Sialkot"
city = get_city()
print(city)

def check_age(age):
    if age >= 18:
        return True
    else:
        return False
is_adult = check_age(23)
print(is_adult)            

def check_budget(budget, expense):
    if budget >= expense:
        return True
    else:
        return False
is_within_budget = check_budget(5000, 3500)
print(is_within_budget)

# Topic 3: Storing Returned Values

def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(2000, 5)
if total >= 5000:
    print("Boxing gloves are expensive")
else:
    print("Hand wraps are inexpensive") 

def calculate_marks_percentage(obtained_marks, total_marks):
    return (obtained_marks/total_marks)*100
percentage = calculate_marks_percentage(450, 500)
if percentage >= 80:
    print("Excellent Performance")  
else:
    print("Keep Practicing")       

# Topic 4: Using returned values again

def calculation(price, quantity):
    return price * quantity
def check_order(total):
    if total >= 50000:
        return "Free Delivery"
    else:
        return "Delivery Charges Apply"
order_total = calculation(1200, 40)
delivery_status = check_order(order_total)
print("Order Total:", order_total)
print("Delivery Status:",delivery_status)

def product(price, quantity):
    return price * quantity
def check_discount(total):
    if total >= 10000:
        return "Discount Available"
    else:
        return "No Discount"
order_totl_amount = product(500, 16)
discount_status = check_discount(order_totl_amount)
print("Order Total Amount:", order_totl_amount)
print("Discount Status:", discount_status)

# Topice 5: Returning Different Values Based on Conditions
def product_rating(rating):
    if rating >= 4:
        return "Excellent"
    elif rating >= 3:
        return "Good"
    else:
        return "Needs Improvements"
result = product_rating(2)
print(result)

def check_stock(stock):
    if stock >= 200:
        return "Stock Available"
    elif stock >= 50:
        return "Stock is Low"
    else:
        return "Out of Stock"
result = check_stock(0)
print(result)                

# Topic 6: Returning Multiple Values from a Function

def calculate_product(price, quantity):
    total = price * quantity
    return total, quantity
result = calculate_product(250, 16)
total_amount, item_quantity = calculate_product(450, 15)
print("Total Amount:", total_amount)
print("Item Quantity:", item_quantity)
print(result)


def calculate_marks(obtained_marks, total_marks):
    percentage = (obtained_marks/total_marks)*100
    return percentage, obtained_marks
percentage, marks = calculate_marks(637, 1200)
print(f"Percenage:{percentage:.2f}%")
print("Obtained Marks:", marks)

# Topic 7: Combining return with Previous Python Concepts

def calculate_total(price, quantity):
    return price * quantity
def calculate_discount(total):
    if total >= 10000:
        return total * 0.10
    else:
        return 0
order_total = calculate_total(2500, 12)
discount = calculate_discount(order_total)
final_amount = order_total - discount
print("Order Total:", order_total)
print("Discount:", discount)
print("Final Amount:", final_amount)        


def calculate_total(price, quantity):
    return price * quantity
def check_stock(stock):
    if stock >= 20:
        return "Stock Available"
    elif stock > 5:
        return "Stock is Low"
    else:
        return "Out of Stock"
order_total = calculate_total(1500, 12)
stock_status = check_stock(15)
print("Order Total:", order_total)
print("Stock Status:", stock_status)


# Today's practice is complete.
# I practiced using the return statement in Python functions
# and learned the difference between return and print().
# I practiced returning different types of values, including
# numbers, strings, and Boolean values.
# I also practiced storing returned values in variables,
# using returned values in conditional statements, and passing
# returned results from one function to another.
# I practiced returning different values based on conditions
# and returning multiple values from a single function.
# Finally, I combined return with previous Python concepts,
# including variables, arithmetic operators, and conditional
# statements, through practical examples.
