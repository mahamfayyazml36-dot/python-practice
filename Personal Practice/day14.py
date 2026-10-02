# My Day 14 Python Practice
# Name: Maham Fayyaz
# What I learned today: Strings
# (indexing, negative indexing, slicing, string methods,
# lower, upper, capitalize, title, strip, replace, find,
# count, startswith, endswith, in, not in, split, len,
# f-string, escape characters, and multiline strings)

name = 'Maham Fayyaz'
country = 'Pakistan'
field = "Computer sceince"
goal = "AI Researcher"

print(name[5:12])
print(goal[1])
print(country)
print(field)
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])
print(goal[:2])
print(goal[0:13])
print(goal[-11:])
print(goal[:-11])
print(field.lower())
print(goal.upper())
city = "sIALKOT"
print(city.capitalize())
sister_name = 'jannat fiaz'
print(sister_name.title())
intro = "  hello! how are you?  "
print(intro.strip())
course = 'data science'
print(course.replace('data science', "NLP"))
print(country.find("a"))
print(country.find("Z"))
fruit = 'Banana'
print(fruit.count("n"))
print(fruit.count("a"))
world_city = "Pakistan"
print(world_city.startswith("Pak"))
print(world_city.startswith("Land"))
print(world_city.endswith("istan"))
print(world_city.endswith("Ind"))
battle = "World War 1"
print("World" in battle)
book = "Mathematics"
print("green" not in book)
sentence = "I am learning in python"
sentences = sentence.split()
print(sentences)
print(len(sentences))

name = "Maham Fayyaz"
age = 19
field = 'computer science'
print(f"My name is {name}. I am {age} years old and I study {field}.")
name = "Maham Fayyaz"
country = "Pakistan"
goal = "AI Researcher"
print(f"My name is {name}. I am from {country}. My goal is to become an {goal}.")

print("Python\nProgramming")
print("student Name: Maham\nFather Name: Fayyaz")
print("Father Name:\tMuhammad Fayyaz")
print("My name is \"Maham Fayyaz.\" I am from \"Silakot.\" My goal is to become an \"AI Researcher\".")
message = """Hello Maham
Welcome to Python
Today we are learning Strings"""
print(message)

soldier_name = "Ali Khan"
rank = "Captain"
country = "Pakistan"
unit = "Army Rangers"
mission = "Border security"
print(soldier_name)
print(soldier_name[0])
print(soldier_name[7])
print(rank.upper())
print(unit.lower())
print(mission.endswith("security"))
print("security" in mission)
print(soldier_name.count("a"))
print(unit.startswith("Army"))
words = mission.split()
print(words)
print(len(words))
print(mission.find("Border"))
print(f"My name is {soldier_name}. I am a {rank} in the Pakistan Army. I serve in the {unit} unit, and my current mission is {mission}.")

# Today's practice is complete.
# I practiced strings using indexing, negative indexing,
# slicing, string methods, searching, counting, checking
# string content, splitting text, and counting words.
# I also practiced f-strings, escape characters (\n, \t, \"),
# and multiline strings.
# I combined these String concepts in a real-world
# Army Soldier Profile practice.