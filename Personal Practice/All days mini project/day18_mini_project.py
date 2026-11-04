# My Day 18 Python Mini Project
# Name: Maham Fayyaz
# Project: Community Event Planning & Readiness Report
# Concepts: Return, Conditions, Multiple Return Values & Previous Concepts

event_name = "Armed Forces Solidarity Day"
event_location = "Army Public School & College (APS),Ordnance Road Rawalpindi"
event_type = "Community Assembly & Cultural Event"
def expected_guests(guests):
    return guests
total_guests = expected_guests(800)
def venue_capacity_check(expected_guests, venue_capacity):
    if expected_guests <= venue_capacity:
        return "Venue Ready"
    else:
        return "Venue Capacity Insufficient" 
venue_capacity = venue_capacity_check(total_guests, 1000)

total_budget = 600000
estimated_expenses = 580000
def budget_status(total_budget, estimated_expenses):
    if estimated_expenses <= total_budget:
        return "Budget Sufficient"
    else:
        return "Budget Insufficient"
check_budget_status = budget_status(total_budget, estimated_expenses)            

def budget_venue_status(venue_status, budget_status):
    return venue_status, budget_status
venue_information,budget_information = budget_venue_status(venue_capacity, check_budget_status)    

def final_readiness(venue_status, budget_status):
    if venue_status == "Venue Ready" and budget_status == "Budget Sufficient":
        return("Event Ready")
    else:
        return("Event Not Ready")
final_result = final_readiness(venue_capacity, check_budget_status) 
print("~~~~Final Community Event Planning & Readiness Report~~~~")
print("Expected Guests:", total_guests)           
print("Venue Capacity Check:", venue_capacity)
print("Total Budget:", total_budget)
print("Estimated Expenses:", estimated_expenses)
print("Budget Status:", check_budget_status)
print("Budget and Venue Status:", venue_information, budget_information)
print("Final Readiness:", final_result)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Thank you!~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Today's mini project is complete.
# I practiced return values and storing returned results.
# I also practiced conditions and returning multiple values.
# Practiced and completed by: Maham Fayyaz