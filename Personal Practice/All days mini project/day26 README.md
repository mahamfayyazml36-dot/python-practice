# Mini Project 26 - Student Marks Data Transformation

This is my twenty-sixth Python mini project (Day 26 - List Comprehension & Data Transformation + Previous Concepts).

## Concepts Practiced

1. List Comprehension
2. Filtering with Conditions
3. Conditional Expressions
4. Data Transformation
5. Nested List Comprehension
6. Flattening Nested Lists
7. Grade Classification
8. Pass/Fail Classification
9. `zip()` Function
10. Structured Data Transformation

## What It Does

The program takes student names and marks and transforms the data using list comprehensions.

It calculates each student's Pass/Fail status and grade based on their marks. Finally, it uses `zip()` to combine the transformed data into structured student records.

## Grade System

- 90+ → A
- 80–89 → B
- 70–79 → C
- 50–69 → D
- Below 50 → Fail

## Example Output

```text
Name ['Ali', 'Maham', 'Maria', 'Jannat', 'Ahmed']
Student Marks: [95, 33, 88, 67, 81]
Status: ['Pass', 'Fail', 'Pass', 'Pass', 'Pass']
Grade: ['A', 'Fail', 'B', 'D', 'B']

[
    {'Name': 'Ali', 'Marks': 95, 'Status': 'Pass', 'Grade': 'A'},
    {'Name': 'Maham', 'Marks': 33, 'Status': 'Fail', 'Grade': 'Fail'},
    {'Name': 'Maria', 'Marks': 88, 'Status': 'Pass', 'Grade': 'B'},
    {'Name': 'Jannat', 'Marks': 67, 'Status': 'Pass', 'Grade': 'D'},
    {'Name': 'Ahmed', 'Marks': 81, 'Status': 'Pass', 'Grade': 'B'}
]

Project Completed!
```

## Author

Maham Fayyaz