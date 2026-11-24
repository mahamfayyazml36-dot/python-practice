# My Day 28 Python Mini Project
# Name: Maham Fayyaz
# Project: Custom Multiplication Table Generator
# What I practiced today: Iterators & Custom Iteration
# (Classes, Objects, Multiple Parameters, __iter__(), __next__(),
# StopIteration, for Loop, and f-Strings)


class MultiplicationTable():
    def __init__(self,number,start,end):
        self.number = number
        self.current = start
        self.end = end
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current <= self.end:
            result = self.number * self.current
            line = f"{self.number} X {self.current} = {result}"
            self.current += 1
            return line
        raise StopIteration    

#table = MultiplicationTable(12,1,10)
#print(table.number)
#print(table.current)
#print(table.end)
table = MultiplicationTable(12,1,10)
print("============Custom Multiplication Table Generator============")
for number in table:
    print(number)
print("=====================Project Completed!!=====================")    

# Today's Day 28 mini project is complete.