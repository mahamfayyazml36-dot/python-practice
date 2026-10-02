# My Mini Project 14: Army Cyber Defense Text Analyzer
# Name: Maham Fayyaz
# What it does: Analyze army mission text, search important words,
# check mission status, and generate a mission report.
# What I learned: strings (indexing, slicing, split, find, count,
# startswith, endswith, in, not in, string methods),
# f-string, len(), if-else, and combining previous concepts.

soldier_name = "Maham Fayyaz"
rank = "Captain"
unit = "Cyber Defense unit"
location = "Pakistan"
mission = "Protect Army computer systems from cyber threats"
print("~~~~~~~~~~ SOLDIER PROFILE ~~~~~~~~~~")
print(f"Name:\t{soldier_name}\nRank:\t{rank}\nUnit:\t{unit}\nLocation:\t{location}\nMission:\t{mission}")
print("~~~~~~~~~~ MISSION ANALYSIS ~~~~~~~~~~")
print("Total character:" ,len(mission))
missions = mission.split()
print(missions)
total_word = len(missions)
print("Total word:", total_word)
print("First character:", mission[0])
print("Last character:", mission[-1])
print("First word:", missions[0])
print("First word:", mission[0:7])
print("Last word:", missions[-1])
print("~~~~~~~~~~  MISSION WORD SEARCH ~~~~~~~~~~")
check = "cyber" in mission
print("Is cyber in mission?", check)
checks = "virus" in mission
print("Position of 'cyber':", mission.find("cyber"))
word_count = mission.count("cyber")
print("How many times 'cyber' appears:", word_count)
print()
print("Is virus in mission?", checks)
print("\n~~~~~~~~~~ MISSION STATUS ~~~~~~~~~~")
if "Protect" in mission:
    mission_status = "ACTIVE"
    print("Mission Status:", mission_status)
else:
    mission_status =  "CHECK REQUIRED"
    print("Mission Status:", mission_status)
print("~~~~~~~~~~ MISSION REPORT ~~~~~~~~~~")
print(f"Soldier: {soldier_name}\nRank: {rank}\nUnit: {unit}\nLocation: {location}\nMission: {mission}\nMission Status: {mission_status}\nTotal Words: {total_word}")

# Mini Project day 14 complete.
# This program is a text analyzer for an Army Cyber Defense mission
# using strings and previous Python concepts.
# It analyzes mission details, searches words, counts occurrences,
# checks mission status, and generates a final report.