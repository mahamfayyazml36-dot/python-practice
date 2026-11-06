# My Day 19 Python Mini Project
# Name: Maham Fayyaz
# Project: Emergency Response & Rescue Operations Tracker
# What I practiced today: Scope — Local and Global Variables
# (Local Variables, Global Variables, Local vs Global Scope,
# Same Variable Name, global Keyword, Functions, Parameters,
# Arguments, Return, and Conditional Statements)

centre_name = "Sialkot Emergency Response Centre"
available_rescue_units = 12
active_operations = 0

def report_emergency(caller_name, location):
    emergency_type = "Road Accident"
    return caller_name, location, emergency_type
emergency_report = report_emergency("Ali Raza", "Sialkot Cantt")
print(emergency_report)

def check_emergency_priority(injured_people):
    if injured_people >= 5:
        return "High Priority"
    else:
        return "Normal Priority"
emergency_priority = check_emergency_priority(6)
print(emergency_priority)

def assign_rescue_unit(priority):
    global available_rescue_units
    if priority == "High Priority" and available_rescue_units > 0:
        available_rescue_units = available_rescue_units - 1
        return "Rescue Unit Assigned"
    else:
        return "No Rescue Unit Available"    
rescue_unit_result = assign_rescue_unit("High Priority")
print(rescue_unit_result)
print(available_rescue_units)

def check_operation_status(rescue_assigned):
    active_operations = 1
    if rescue_assigned == "Rescue Unit Assigned":
        return "Operation Active"
    else:
        return "Operation Pending"
operation_status_result = check_operation_status("Rescue Unit Assigned")   
print(operation_status_result)
print(active_operations)

def generate_operation_summary(caller_name,location,emergency_type,priority,rescue_status,operation_status):
    return centre_name,caller_name, location, emergency_type, priority, rescue_status, operation_status
summary = generate_operation_summary("Ali Raza", "Sialkot Cantt", "Road Accident", "High Priority", "Rescue Unit Assigned", "Operation Active")
print(summary)    

# Today's mini project is complete.
# I practiced using local and global variables in a real-world
# emergency response system and used the global keyword to update
# available rescue units.