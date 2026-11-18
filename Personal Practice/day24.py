# My Day 24 Python Practice
# Name: Maham Fayyaz
# What I learned today: Nested Functions & Function Workflow
# (Nested Functions, Inner & Outer Functions, Return Values,
# Function-to-Function Data Flow, Parameters, and Function Workflow)


# 1.
def bank(customer1, customer2):
    
    def total_amount(salary, days):
        amount = customer1 + customer2
        total_incom = salary * days
        print( total_incom)
        return amount
    return total_amount(500, 30)
result = bank(12000, 500000)    
print(result)

# 2.
def process_sentence(sentence):
    def clean_line():
        return sentence.strip().title()
    return clean_line()
print(process_sentence("my name is maham fayyaz."))        

# 3.
def get_name():
    return "Jannat Fayyaz"
def intro(name):
    return "Hello " + name +"!"
name = get_name()    
message = intro(name)
print(message)    

# 4.
def get_marks():
    return 85
def calculate_percentage(marks):
    return "Maham got " + str(marks) + "% in metric."
marks = get_marks()
message = calculate_percentage(marks)
print(message)    

# Today's practice is complete.