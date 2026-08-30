
# ============================================================
# Python Real-World Project: Pakistan-India May 10, 2025 Conflict Analysis
#
# Practiced and Developed by: Maham Fayyaz
# Completed after: Day 4 Python Learning (Variables, Operators, Conditionals, Loops)
#
# Project Description:
# - Analysis of conflict timeline and historical data.
# - Storing event datasets using Lists, Nested Lists, and Dictionaries.
# - Classifying event severity using Conditional Statements (if-elif-else).
# - Iterating through timeline data using for loops, enumerate(), and zip().
# ============================================================


# ================================================================
# Pakistan-India May 10, 2025 Conflict Analysis
# Project Introduction
# ============================================================

# Store basic project information

project_title = "Pakistan-India May 10, 2025 Conflict Analysis"
country_1 = "Pakistan"
country_2 ="India"
important_date = "10 May 2025"
project_type ="Real-World Python Project"

# Get user information through input

user_name = input("Enter the User Name:")
country = input("Enter the Country Name:")
user_interest = input("Enter your interest in this project:")

# Display project introduction

print("================================================================")
print(project_title)
print("================================================================")
print("Project Title:", project_title)
print("Country One:", country_1)
print("Country Two:", country_2)
print("Important Date:", important_date)
print("Project Type:", project_type)

# Display user information

print("================================================================")
print("welcom",user_name,"!")
print("================================================================")
print("Your Country:", country)
print("Your Interest:", user_interest)
print("================================================================")

# ================================================================ 
# STEP 3 - CONFLICT / EVENT DATA 
# ================================================================ 
# Store conflict events using a nested list 
# Each event contains: Date, Event Name, Event Status

conflict_event =[
    ["10 May 2025", "Military Escalation", "Major Event"],
    ["10 May 2025", "Drone and Missile Exchanges", "Major Event"],
    ["10 May 2025", "Artillrey Exchanges", "Military Event"],
    ["10 May 2025", "Ceasefire Announcement", "De-escalation"],
    ["10 May 2025", "Conflict De-escalation", "Important Event"]
]

# Store country and conflict information in a dictionary

country_information ={
    "country_1" : "Pakistan",
    "country_2" : "India",
    "Date" : "10 May 2025",
    "conflict_type" : "Militry conflict"
}

# Display conflict event data

print("CONFLICT EVENTS")
print("================================================================")
print(conflict_event)

# Display country information

print("\n================================================================")
print("COUNTRY INFORMATION")
print("================================================================")
print(country_information)

# ================================================================ 
# STEP 4 - MAY 10 TIMELINE 
# ================================================================
# Store important events according to the timeline

may_10_timeline = [
    ["10 May 2025", "Morning", "Military Exchanges"],
    ["10 May 2025", "Afternoon", "Continued Military Exchanges"],
    ["10 May 2025", "Later", "Ceasefire Announcement"]
]

# Display May 10 timeline

print("================================================================")
print("MAY 10 TIMELINE")
print("================================================================")
print(may_10_timeline)

# ================================================================ 
# STEP 5 - EVENT CLASSIFICATION 
# ================================================================

print("================================================================")
print("EVENT CLASSIFICATION")
print("================================================================")

# Store the status of an event

event_status = "Major Event"

# Classify the event using if, elif and else

if event_status == "Major Event":
    print("This is an Major Event.")

elif event_status == "Military Event":
    print("This is an Military Event.")

elif event_status == "De-escalation":
    print("This is an De-escalation Event.")

else:
    print("This is an Important Event.")

# ================================================================ 
# STEP 6 - MULTIPLE CONDITIONS 
# ================================================================

print("================================================================")
print("MULTIPLE CONDITION")
print("================================================================")

# Store event status, date and ceasefire status

event__status = "Major Event"
event__date = "10 May 2025"
is_ceasefire_announced = True

# Use AND to check two conditions together

if event__status == "Major Event" and event__date == "10 May 2025":
    print("This is a major event on May 10, 2025.")

# Use OR to check multiple possible conditions

if event__status == "Major Event" or is_ceasefire_announced == False:
    print("This event is important for the analysis.")

# Use NOT to reverse a Boolean condition

if not is_ceasefire_announced:
    print("Ceasefire was not announced.")

else:
    print("Ceasefire was announced.")             

# ================================================================ 
# STEP 7 - EVENT SEARCHING 
# ================================================================

print("================================================================")    
print("EVENT SEARCHING")
print("================================================================")   

# Search for a specific event

search_event = "Drone and Missile Exchanges"

# Loop through all conflict events

for event in conflict_event:

    # Check whether the event name matches the search event

    if event[1] == search_event:
        print("Found Event:", event)

# ================================================================ 
# STEP 8 - EVENT NUMBERING 
# ================================================================

print("================================================================")    
print("EVENT NUMBRING")
print("================================================================") 

# Use enumerate() to give each event a number

for number, event in enumerate(conflict_event, start=1):
    print("Event", number, ":", event)

# ================================================================ 
# STEP 9 - DATES + EVENTS 
# ================================================================

print("================================================================")    
print("DATE + EVENT")
print("================================================================")  

# Display the date and event name separately

for event in conflict_event:
    print("Date:", event[0], "| Event:", event[1])

# ================================================================ 
# STEP 10 - IMPORTANT EVENT STOP 
# ================================================================

print("================================================================")  
print("IMPORTANT EVENT STOP")
print("================================================================")  

# Search for an important event

for event in conflict_event:
    print("Checking Event:", event[1])
    
    # Stop the loop when the important event is found

    if event[1] == "Ceasefire Announcement":
        print("Important Event Found:", event[1])
        break

# ================================================================ 
# STEP 11 - SKIP UNWANTED DATA 
# ================================================================

print("================================================================")  
print("SKIP UNWANTED DATA")    
print("================================================================") 

# Use continue to skip unwanted data

for event in conflict_event:

    # Skip De-escalation events

    if event[2] == "De-escalation":
        continue
    
    print("Event:", event[1], "| Status:", event[2])

# ================================================================ 
# STEP 12 - EVENT COUNTING 
# ================================================================

print("================================================================") 
print("EVENT COUNTING")
print("================================================================") 

# Start counters from zero

total_event = 0
major_event = 0

# Count total events and major events

for event in conflict_event:
    total_event = total_event + 1

    # Count events classified as Major Event

    if event[2] == "Major Event":
        major_event = major_event +1

    # Display final counts after the loop

print("Total Events:", total_event)
print("Total Major Events:", major_event)

# ================================================================ 
# STEP 13 - SIMPLE STATISTICS 
# ================================================================    

print("================================================================") 
print("SIMPLE STATISTICS")
print("================================================================") 

# Calculate the percentage of Major Events

major_event_percentage = (major_event / total_event) * 100

# Display simple statistics

print("Major Event:", major_event)
print("Total Event:", total_event)
print("Major Event Percentage:", major_event_percentage, "%")     

# ================================================================ 
# STEP 14 - FINAL REPORT 
# ================================================================

print("================================================================") 
print("FINAL CONFLICT ANALYSIS REPORT")
print("================================================================") 

# Display project information

print("Project Title:", project_title)
print("Countreis:", country_1, "and", country_2)
print("Important Date:", important_date)
print("Conflict Type:", country_information["conflict_type"])
print("-----------------------------------------------------------------") 

# Display statistical results

print("Total Event:", total_event)
print("Major Event:", major_event)
print("Major Event Percentage:", major_event_percentage)
print("-----------------------------------------------------------------") 
print("EVENT SUMMARY")

# Display all events with numbering

for number, event in enumerate(conflict_event, start = 1):
    print(number, "-" ,event[0],"-" ,event[1], "-" ,event[2])
print("================================================================") 
print("END FOR REPORT")
print("================================================================")    



# ============================================================
# PROJECT SUMMARY & KEY LEARNING OUTCOMES
# ============================================================
# 1. Real-World Data Structuring:
#    - Organized timeline events using nested lists and key-value dictionary formats.
#
# 2. Dynamic Input Handling:
#    - Captured and processed dynamic input data using input() and formatted print statements.
#
# 3. Control Flow & Iteration:
#    - Applied for loops and enumerate() to extract structured event details.
#    - Utilized if-elif-else logic to classify conflict severity levels automatically.
#
# Status: First Independent Python Real-World Project Completed Successfully!
# ============================================================