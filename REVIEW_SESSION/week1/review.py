#1.Number classifier
n =int(input("Enter the number:"))
if(n<0):
    print("The number is negative")
elif(n>0):
    print("The number is positive")
else:
    print("The number is zero")
if n%2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#2.Grade calculator
mark = int(input("Enter the mark:"))
if mark >=0 and mark <=20:
    print("F")
elif mark >20 and mark<=40:
    print("D")
elif mark >40 and mark <=60:
    print("C")
elif mark >60 and mark <=80:
    print("B")
else:
    print("A")
# 3.Multiplication table
n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
# 4.contact book
contact ={}
def add_contact():
    name =  input("Enter the name:")
    number = int(input("Enter the number:"))
    contact[number] = {name:"name"}
add_contact()
# 5.student
class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def show(self):
        print(self.name)
        print(self.grade)
s1 = student("Ravi",11)
s2 = student("sheela",10)
s1.show()
s2.show()