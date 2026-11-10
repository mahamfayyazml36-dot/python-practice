# My Day 22 Python Mini Project
# Name: Maham Fayyaz
# Project: Boyle's Law Experimental Data Analyzer
# What I practiced today: Data Processing
# (map(), filter(), reduce(), sorted(), and Lambda Functions)


pressure = [2, 4, 5, 8, 10]
volume = [10, 5, 4, 2.5, 2]
boyles_values = map(lambda first, second : first * second, pressure,volume)
result = list(boyles_values)
print("Experimental readings:",result)
valid_values = filter(lambda number : number == 20, result) 
filtered_values = list(valid_values)
sorted_values = sorted(filtered_values)
from functools import reduce
total_constant = reduce(lambda first, second : first + second, sorted_values)
print("Experimental Reading Total:",total_constant)

# Today's mini project is complete.
# I practiced Data Processing using map(), filter(), reduce(),
# sorted(), and Lambda Functions with Boyle's Law