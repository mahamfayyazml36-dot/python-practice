# My Day 28 Python Practice
# Name: Maham Fayyaz
# What I learned today: Iterators & Custom Iteration
# Iterable, Iterator, iter(), next(), StopIteration
# for loop with Iterators
# while loop with Iterators
# Custom Iterator using __iter__() and __next__()
# Classes, Objects, __init__(), self, Parameters
# Multiple Objects and Object Attributes


name = {
    "ayesha_age" : 19,
    "Maham_age" : 29,
    "Noor_age" : 28
}
iterator = iter(name.items())
print(next(iterator))
print(next(iterator))
print(next(iterator))

addition = {"Eddition1", "Eddition2", "Eddition2","Eddition3"}
for additions in addition:
    print(additions)

number = range(10,20,3)
iterator = iter(number)
while True:
    try:
        one_by_one = next(iterator)
        print(one_by_one)
    except StopIteration:
        break

class student:
    def __init__(self,name):
        self.name = name
student_1 = student("Jannat Fiaz")
student_2 = student("Maham")
print(student_1.name)
print(student_2.name)

    
class Mynumber:
    def __init__(self):
        self.number = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.number <= 5:
            value = self.number
            self.number += 1
            return value
        raise StopIteration 
numbers = Mynumber()

#print(numbers.number)          
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))
for number in numbers:
    print(number)

class Person:
    def __init__(self,name,age,height,subject,percentage):
        self.name = name
        self.age = age
        self.height = height
        self.subject = subject
        self.percentage = percentage
person_1 = Person("Maham Fayyaz", 19, 5.2, "Biology", 70)
person_2 = Person("Maria Fiaz", 23, 5.1, "Computer science", 75)
print(person_1.name)
print(person_1.age)
print(person_1.height)
print(person_1.subject)        
print(person_1.percentage)
print(person_2.name)
print(person_2.age)
print(person_2.height)
print(person_2.subject)        
print(person_2.percentage)

number  = range(1,6)
print(len(number))
iterator = iter(number)
while True:
    try:
        one_by_one = next(iterator)
        if one_by_one < 7:
            print(one_by_one)
        else:
            print("Keep Practice!")
    except StopIteration:
        break

# Today's practice is complete.