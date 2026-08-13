# INPUT METHOD 
name = input("Enter your Name:")
age = input("Enter your Age:")
height = input("Enter your Height:")
city = input("Enter your city:")
country = input("Enter your country:")
college_name = input("Enter your College Name:")
education = input("Enter your Education:")
field = input("Enter your feild:")
print(f"My name is {name}.I am {age} years old.My height is {height}.I am live in {city}, {country}.I studied at {college_name}. I learned {education} and my field is {field}.")

# NORMAL PRINT
# 1.
print("My name is", "MAHAM FAYYAZ.")
#2.
print("Hello", "How are you?")
#3.
print("I am fine.", "What about you Bro?")

# Using Separator
print("Hello", "World.", sep="New")
print("Hello", "World.", sep=" Old ")

# Using end
print("HI", end=" ")
print("Maria Fayyaz.")

# Using Escap Sequences
print("HELLO!\nHow are you?")          # Using \n
print("My name is Maham Fayyaz.\nI am 19 years old.")
print("My college name is\tGovt Graduate College For Women HajjiPura Sialkot." )  # Using \t
print("Hello my \"Ai sir\"")    # Using ""

# f-String and .f format

#1.
name = "Maham Fayyaz"
percentage = 70
print(f"My name is {name}.I get in metric {percentage}%.")
#2.
print("My name is {}.I get in metric {}%.".format(name,percentage))