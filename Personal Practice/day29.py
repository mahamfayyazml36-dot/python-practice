def introduction():
    yield "Name: Maham"
    yield "Age: 19"
    yield "Height: 5 Feet 1 inch"
    yield "Education: ICS Economics"
genrator = introduction()
print(next(genrator))
print(next(genrator))
print(next(genrator))
print(next(genrator))

def number(number_1, number_2):
    addition = number_1 + number_2
    return addition
result = number(12,32)
print(result)    

def calculation(number_one,number_two):
    addition = number_one + number_two
    subtraction = number_one - number_two
    multiplication = number_one * number_two
    yield addition
    yield subtraction
    yield multiplication
result = calculation(12,36)
for final_result in result:
    print(final_result)

def number():
    for data in range(5):
        yield data
for result in number():
    print(result)

def data_generator():
    for batch_number in range(100):
        batch = [batch_number * 10 + l for l in range(10)]
        yield batch
for data in data_generator():
    print(data)        

students = [
    {"name": "Ali", "marks": 80},
    {"name": "Sara", "marks": 90},
    {"name": "Ahmed", "marks": 65},
    {"name": "Maham", "marks": 95},
    {"name": "Ayesha", "marks": 72}
]
def students_data():
    yield students[0]
    yield students[1]
    yield students[2]
    yield students[3]
    yield students[-1]
for data in students_data():
    print(data) 

def student_data():
    for student in students:
        yield student
for data in student_data():
    print(data)     
    
def student_data():
    for student in students:
        if student["marks"] >= 80:
            yield student["marks"]  

total_marks = 0
count = 0

for data in student_data():
    total_marks += data
    count += 1
average = total_marks / count
print(average)    
                 