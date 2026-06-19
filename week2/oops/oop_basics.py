class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def study(self):
        print(f"{self.name}  is studying ")
class BankAccount:
    def __init__(self):
        self.balance = 50000
    def deposit(self,amount):
        self.balance += amount
        print(f"The balance in the account is {self.balance}")
    def withdraw(self,amount):
        self.balance -= amount
        if(self.balance <= 0):
            print("The account has no balance please deposit with some amount")
            self.balance = 0
        print(f"The balance in the account is {self.balance}")
if __name__ == __main__:
    student_1 = Student("lokesh",10)
    student_2 = Student("ravi",8)
    bankaccount_1 = BankAccount()
    bankaccount_2 = BankAccount()
    student_1.study()
    student_2.study()
    print("")
    bankaccount_1.deposit(25000)
    bankaccount_1.withdraw(36750)
    print("")
    bankaccount_2.withdraw(55000)
    bankaccount_2.deposit(10000)