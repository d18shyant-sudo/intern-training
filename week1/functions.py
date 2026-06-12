# 1. CONTACT BOOK
contact={}
def add_contact():
    name=input("Enter the name:")
    number=int(input("Enter the number:"))
    contact[name]={"number":number}
def find_contact():
    query = input("Enter the name:")
    for data,detail in contact.items():
        if(query == data):
            print(detail['number'])
def list_contact():
    for data,detail in contact.items():
        print(f"Name :{data}\nContact_no:{detail['number']}")
while(True):
    print("1.ADD CONTACT\n2.FIND CONTACT\n3.LIST CONTACT\n4.EXIT\n")
    choice = int(input("Enter the number:"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        find_contact()
    elif choice == 3:
        list_contact()
    elif choice == 4:
        break;
    else:
        print("Invalid choice")
# 2. To-Do list
Task=[]
def add_task():
    add_task = input("Enter the task:")
    Task.append(add_task)
def remove_task():
    remove_task = input("Enter the task to remove:")
    Task.remove(remove_task)
def show_tasks():
    for task in Task:
        print(task)
    print("")
while(True):
    print("1.ADD TASK\n2.REMOVE TASK\n3.SHOW TASK\n4.EXIT\n")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        show_tasks()
    elif choice ==4 :
        break;
    else:
        print("Invalid choice")

