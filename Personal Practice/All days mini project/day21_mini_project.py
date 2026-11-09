# My Day 21 Python Mini Project
# Name: Maham Fayyaz
# Project: Chemical Solution Concentration Analyzer
# What I practiced today: Lambda Functions
# (Lambda Functions, Parameters, Arguments, Expressions,
# Automatic Return, Calculations, and Conditional Lambda)

solution_name = "Sodium Chloride Solution"
solute_mass = 20
solution_volume = 2


concentration = lambda mass, volume : mass / volume
result = concentration(solute_mass,solution_volume)
print(result)

check_Parameter = lambda concentration_volume : "High Concentration" if concentration_volume >= 10 else "Low concentration"
result = check_Parameter(10)
result2 = check_Parameter(9)
print(result)
print(result2)

# Today's mini project is complete.
# I practiced using Lambda Functions for simple calculations
# and conditional expressions to classify solution concentration.