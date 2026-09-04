# ================================================================
# Day 6 - Control Flow Practice
# Break, Continue and Pass
# ================================================================
# Practice Description:
# This practice focuses on break, continue, and pass statements
# with for and while loops.
# It also includes mixed control-flow exercises using conditions,
# lists, strings, and counters.
# ================================================================

# break with for
# 1
for number in range(1, 10):
    if number == 6:
        break
    print(number)
# 2
for numbers in range(1, 11, 2):
    if numbers == 9:
        break
    print(numbers)
# break with while
number = 10
while number <= 20:
    if number == 18:
        break
    print(number)
    number = number + 1    
# continue with for
# 1
for count in range(1, 10):
    if count == 6:
        continue
    print(count) 
# 2
name = "Maham"
for charector in name:
    if charector == "h":
        continue
    print(charector)
# 3
names = ["Php lerval", "Java", "Java scripts"]
for name_list in names:
    if name_list == names[1]:
        continue
    print(name_list)
# continue with while
# 1
number = 1
while number <= 10:
    if number == 7:
        number = number + 1
        continue
    print(number)    
    number = number + 1    
# 2
name = "Maham Fayyaz"
index = 0
while index < len(name):
    if name[index] == "a":
        index =index + 1
        continue
    print(name[index])
    index = index + 1

# 3 
names = ["Maham", "Dr.soren", "Leon", "PHP"]
number = 0
while number < len(names):
    if names[number] == names[2]:
        number = number + 1
        continue
    print(names[number])
    number = number + 1
# for + pass Practice
# 1
for number in range(1, 11):
    if number == 8:
        pass
    print(number)
# 2
name = "Jannat Fayyaz"
for personality_name in name:
    if personality_name == "a":
        pass
    print(personality_name)    

# while + pass
# 1
numbers = 1
while numbers <= 10:
    if numbers == 6:
        pass
    print(numbers)
    numbers = numbers + 1
# 2
course = ["ML", "NLP", "SQL", "Java", "HTML"]
number = 0
while number < len(course):
    if course[number] == course[3]:
        pass
    print(course[number])
    number = number + 1

# Mixed Practice — for loop (pass, continue, break)

# 1
numbers =[2, 5, 6, 7, 9, 11, 14, 17, 20] 
for number in numbers:
    if number%2 == 0:
        continue
    elif number == 17:
        break
    else:
        print(number)
# 2
numbers = [2, 5, 8, 10, 13, 15, 17, 20]
for numbere in numbers:
    if numbere%2 == 0:
        continue
    elif numbere == 13:
        pass
    elif numbere == 17:
        break
    else:
        print(numbere)
# while + break + continue + pass
number = 1
while number <= 15:
    if number % 2 == 0:
        number = number + 1
        continue
    elif number == 9:
        pass
        print(number)
        number = number + 1    
    elif number == 13:
        break
    else:
        print(number)
        number = number + 1


# ================================================================
# Day 6 Practice Completed
# Concepts Practiced:
# break, continue, pass, for loop, while loop,
# if/elif/else, lists, strings, len(), counters,
# and basic control-flow problem solving.
# ================================================================