# todo list mini app
tasks = []

# function for add task
def add_task():
    name = input("enter the of name todo :")
    for t in tasks:
        if name == t[0]:
            print("task with this name is already booked")
            return
    todo = input("enter your task : ")
    task = [name,todo]
    tasks.append(task)
    print("\n ✔task sucessfull add")
    print("-------------------")

# view task
def view_task():
    if not tasks:
        print("NO task here")
        print("-------------------")
    else:
        num = 0
        for t in tasks:
            num += 1
            print(f"\n===Your {num} task here===")
            print(t[0],":",t[1])
            print("-------------------")

# delete task
def delete_task():
    if len(tasks) == 0:
        print("❌There are no task to delete")
        return
    name = input("enter the task name : " )
    for t in tasks:
        if name == t[0]:
            tasks.remove(t)
            print("\n✔Task are deleted sucessfull")
            print("-------------------")
            return        

    print("not found this task")

# update task 
def update_task():
    if len(tasks) == 0:
        print("❌There are no task to update")
        return
    name = input("enter your task name to update : ")
    for t in tasks:
        if name == t[0]:
            t[1] = input("enter your new task : ")
            print("\n✔Task update sucessfull ")
            print("-------------------")
            return
        
    print("There are no task name like this")

# delete all todo
def clear_task():
    tasks.clear()
    print("\n✔clear all sucessfull")
    print("--------------------------")
    return

# main 
while True:
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Update task")
    print("5. Clear task")
    print("6. Exit")
    
    choice = input("enter your choice : ")
    print("--------------------------")


    # condation
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        clear_task()
    elif choice == "6":
        print("🙃Thanks for using our todo app🙃")
        break
    else:
        print("error")

