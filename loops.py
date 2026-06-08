#1. Multiplication table printing anywhere from 1-10
n = int(input("Enter the table : "))
for i in range(1,11):
    print(f"{n} x {i} "+"=", n*i)
#2. sum of every number from 1 to 100
num = 0 
for i in range(1,101):
    num+=i
print("The sum from 1 to 100 is ",num)
#3.FizzBuzz for 1-50
for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print(f"{i} is FizzBuzz")
    elif i%3 == 0:
        print(f"{i} is Fizz")
    elif i%5 == 0:
        print(f"{i} is Buzz")
    else : 
        print(f"{i} is not applicable for any FizzBuzz rules")
#4. number guessing game
targer=25
while(True):
    n = int(input("Enter the number:"))
    if n<25:
        print("lower")
    elif n>25:
        print("higher")
    else:
        print("You guessed the correct number!")
        break;