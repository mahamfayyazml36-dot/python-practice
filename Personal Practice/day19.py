# My Day 19 Python Practice
# Name: Maham Fayyaz
# What I learned today: Scope — Local and Global Variables
# (Local Variables, Global Variables, Local vs Global Scope,
# Same Variable Name, and the global Keyword)

'''This function calculates a delivery rider's daily earning by multiplying 
the number of deliveries by 500 and adding a customer tip as a bonus. 
It uses local variables inside the function to store the earning, bonus, 
and total earning.'''

def calculate_daily_earning(deliveries):
    earning = deliveries * 500
    bonus = 50
    total_earning = bonus + earning
    return total_earning
result = calculate_daily_earning(45)
#print(earning)
print(result)


'''This function calculates the tax on a product price using a global tax rate. 
It changes the global tax rate inside the function using the global 
keyword and calculates the final tax.'''
tax_rate = 0.05
def calculate_tax(price):
    global tax_rate 
    tax_rate = 0.10
    tax = price * tax_rate
    return tax
result = calculate_tax(5000)    
print(result)
print(tax_rate)

'''This function creates a hospital appointment using a patient name. 
It uses a global variable for the hospital name and a local variable 
for the appointment status. The global variable can be accessed inside 
and outside the function, while the local variable can only be accessed 
inside the function.'''

hospital_name = "Pak Medical Centre Near Defence Road"
def creat_appointment(patient_name):
    appointment_status = "Confirmed"
    print(appointment_status)
    print(hospital_name)
    return appointment_status, patient_name
result = creat_appointment("Maham Fayyaz")
print(hospital_name)
print(result)    
#print(appointment_status)


balance = 50000
def check_balance():
    balance = 25000
    print(balance)
check_balance()

payment = 20000
def check_status():
    global payment
    payment = 5000
    print(payment)
check_status()  


total_visitor = 0
def new_visistor():
    global total_visitor
    total_visitor = total_visitor + 1
    return total_visitor
result1 = new_visistor()
result2 = new_visistor()    
result3 = new_visistor()
print(result1)
print(result2)
print(result3)

# Today's practice is complete.
# I practiced understanding local and global variables,
# learned how Python handles the same variable name in
# different scopes, and practiced using the global keyword.