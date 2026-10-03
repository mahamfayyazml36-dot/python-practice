# My Day 15 Python Practice
# Name: Maham Fayyaz
# What I learned today: String Methods & Formatting
# (lstrip, rstrip, isalpha, isdigit, isalnum, isspace,
# islower, isupper, title, istitle, join, f-string formatting)

name = "  Maham Fayyaz  "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#email = "Email: hunarmand125@gamil.com"
#print(email.removeprefix("Email: "))
#print(name.removeprefix("Hello"))
#prefix = "beginning"
#sufix = "ending.txt"                           # Python 3.9+ introduce removeprefix and removesuffix
#print(sufix.removesuffix(".txt"))

name = "MuhammadFiaz"
print(name.isalpha())
name = "MuhammadFiaz12"
print(name.isalpha())
name = "Maham Fayyaz"
print(name.isalpha())
number = "13"
print(number.isdigit())
number = "sjkg234"
print(number.isdigit())
number = "maham125"
print(number.isalnum())
mail = "hjjskd@gmail.com"
print(mail.isalnum())
father_name = "Muhammad Fayyaz"
print(father_name.isspace())
space = "  "
print(space.isspace())
a = "maham"
b = "MAHAM"
c = "Maham"
d = "maham fayyaz"
print(a.islower())
print(b.islower())
print(c.islower())
print(d.islower())
print(a.isupper())
print(b.isupper())
print(c.isupper())
print(d.isupper())
print(d.title())
print(d.istitle())
skills = ["Python", "C", "C++", "Java"]
result = " ".join(skills)
result2 = ", ".join(skills)
print(result)
print(result2)
date = ["2026", "10", "3"]
result1 = "-".join(date)
print(result1)
skills = ["Python", "AI", "Data Science", "Machine Learning"]
course = "|".join(skills)
print(course)
math = 55
computer = 60.5
urdu = 85
english = 88.5
total = math + computer + urdu + english
percentage = (total/400)*100
print(f"Total: {total:.2f}")
print(f"percentage: {percentage:.2f}%")

# Today's practice is complete.
# I practiced advanced string methods, string validation,
# joining strings, and f-string formatting.
# I also practiced decimal and percentage formatting.