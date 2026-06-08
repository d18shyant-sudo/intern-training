# 1.Number classifier
n = int(input("Enter the number:"))
if(n>0):
    print("The number is positive")
elif(n<0):
    print("The number is negative")
else:
    print("The number is zero")
if(n%2==0):
    print("The number is even")
else:
    print("The number is odd")
# 2. Grade Calculator
grade=int(input("Enter the mark:"))
if (grade>0 and grade < 21):
    print("The Grade is F")
elif (grade>20 and grade < 41):
    print("The Grade is D")
elif (grade>40 and grade < 61):
    print("The Grade is C")
elif (grade>60 and grade < 81):
    print("The Grade is B")    
else:
    print("The Grade is A")    
# 3. login checker
stored_password = "Admin@123"
entered_password = input("Enter the password:")
if(entered_password == stored_password):
    print("Login Successful!")
else:
    print("Login Failed.Incorrect Password")
# 4. largest number among 3 number finder
a =  float(input("Enter the number 1:"))
b =  float(input("Enter the number 2:"))
c =  float(input("Enter the number 3:"))
def find_largest(a,b,c):
    if(a>c and b>c and a==b):
        return "number 1 and 2 is greater"
    elif(b>a and c>a and b==c ):
        return "number 2 and 3 is greater"
    elif(c>b and a>b and c==a):
        return "number 1 and 3 is greater"
    elif (a>b and a>c):
        return "number 1 is greater"
    elif(b>c):
        return "number 2 is greater"
    elif(c>b):
        return "number 3 is greater"
    else:
        return "All numbers are same"
print(find_largest(a,b,c))