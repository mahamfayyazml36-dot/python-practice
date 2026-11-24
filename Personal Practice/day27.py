# My Day 27 Python Practice
# Name: Maham Fayyaz
# What I learned today: Dictionary & Set Comprehension
# Dictionary Comprehension, Filtering, Conditions, Sets, Set Comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]
squares= {}
for number in numbers:
    squares[number] = number ** 2
print(squares)    

numbers = [1,2,3,4,5,6,7,8,9,10]
square = {number : number * 2 for number in numbers}
print(square)

numbers = [2,3,4,5,6]
cube = {number : number ** 3 for number in numbers}
print(cube)

introduction = {
    "name" : "Maham",
    "Age" : 19,
    "height" : 5.1
}
print(introduction["height"])
print(introduction)

numbers = [1,2,3,4,5,6,7,8,9,10,12,13,122,144]
even = {
    number : number ** 2
    for number in numbers
    if number %2 == 0
}
print(even)

unemployment = {
    "Germany" : 5.9,
    "Italy" : 7.9,
    "Spain" : 8.9,
    "France" : 7.4,
    "Poland" : 11.4
}
high_unemployment = {
    country : rate
    for country,rate in unemployment.items() 
    if rate > 7.2
}
print(high_unemployment)

prices = {
    "Bread": 2,
    "Milk": 3,
    "Rice": 5,
    "Oil": 8,
    "Eggs": 4
}
high_price = {
    products : expenses
    for products,expenses in prices.items()
    if expenses > 4
}
print(high_price)

gdp = {
    "Germany": 4,
    "Italy": 2,
    "France": 3,
    "Spain": 5,
    "Poland": 6
}
gDP = {
    country : growth
    for country,growth in gdp.items()
    if growth > 3
}
print(gDP)

print("-------------------SET---------------------")
number = {1,2,2,3,4,5,6,6}
print(number)

number_one = {1,2,2,3,3,4,4,5,6,6}
cube_one = {numbers ** 3 for numbers in number_one}
print(cube_one)

numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,41}
odd = {
    number ** 2
    for number in numbers
    if number %2 != 0
}
print(odd)

gdp_growth = [1.2, 2.5, 3.1, 2.5, 4.2, 1.2, 3.1, 5.0]
unique_gdp = {
    rate
    for rate in gdp_growth
}
print(unique_gdp)

# Today's practice is complete.