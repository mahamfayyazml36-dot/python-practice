# My Day 20 Python Mini Project
# Name: Maham Fayyaz
# Project: Newton's Second Law Experiment
# What I practiced today: Flexible Functions — *args and **kwargs
# (*args, **kwargs, Functions, Parameters, Arguments, Return,
# For Loop, Dictionary, and Calculations)

experiment_name = "Newton's Second Law Experiment"
object_name = "Car"
mass = 1000


def calculate_force(mass, acceleration):
    force = mass * acceleration 
    return force

def experiment_accelerations(*Acceleration):
    print(Acceleration)
    for acceleration in Acceleration:
        print(acceleration)
        force = calculate_force(mass, acceleration)
        print(force)
experiment_accelerations(2, 4, 6, 8)
print("~~~~~~~~~~~~~~~~~~~~~~~Final REsult of Newton's Second Law Experiment~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def experiment_details(**details):
    for key, value in details.items():
        print(key, ":", value)
experiment_details(
    experiment_name="Newton's Second Law Experiment",
    Object_name="Car",
    Mass="1000Kg",
    Location="Science Lab", 
    Duration="2 Hours", 
    Status="completed!!!")        
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

# Today's mini project is complete.
# I practiced using *args for multiple acceleration values
# and **kwargs for flexible experiment details.