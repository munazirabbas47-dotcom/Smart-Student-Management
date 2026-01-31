# 
students = [] #empty list
# add student 
def student_add():

    roll = int(input("enter your roll number : "))
# duplicate roll check
    for s in students:
        if roll == s[0]:
            print("❌student with this roll number is is already added❌")
            return
    name = input("enter your name : ")
    age = int(input("enter your age : "))
    course = input("enter your course : ")
    phone = input("enter your phone number : ")
    student = [roll,name,age,course,phone] #add input into list
    students.append(student) # add list into another list 
    print("\n✔Add sucessfull")
    print("------------------------")

# view student
def view_student():
    if not students:
        print("❌student not found❌")
    else:
        for s in students:
            print("\n=== student list ===")
            print("roll no : ",s[0])
            print("name : ",s[1])
            print("age : ",s[2])
            print("course: ",s[3])
            print("phone no : ",s[4])

# search student
def search_student():
    if len(students) == 0:
        print("❌There are no students for searching")
        return
    roll = int(input("enter roll no to find : "))
    for s in students:
        if roll == s[0]:
            print("\n✔ student found ✔")
            print("roll : ", s[0])
            print("name : ",s[1])
            print("age : ",s[2])
            print("course: ",s[3])
            print("phone no :",s[4])
            return
        
    print("❌student not found❌")

# delete student 
def delete_student():
    if len(students) == 0:
        print("❌There are no students for deleting")
        return
    roll = int(input("enter roll to to delete : "))
    for s in students:
        if roll == s[0]:
            students.remove(s)
            print("\n✔Delete sucessfull")
            return
        
    print("❌student not found❌")

# update student
def update_student():
    if len(students) == 0:
        print("❌There are no students for updating")
        return
    roll = int(input("enter roll to update : "))
    for s in students:
        if roll == s[0]:
            s[1] = input("enter new name : ")
            s[2] = int(input("enter new age : "))
            s[3] = input("enter new course : ")
            s[4] = input("enter new phone number : ")
            print("\n✔Update sucessfull ")
            return 
        
        print("❌student not found❌")

# delete all student
def delete_all_student():
    students.clear()
    print("\n✔Clear sucessfull")
    return

# main 
while True:
    print("\n ===well come to our project=== ")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Delete all")
    print("7. Exit")


    chose = input("enter your choice :")
    print("------------------------")

    if chose == "1":
        student_add()

    elif chose == "2":
        view_student()
    
    elif chose == "3":
        search_student()
    
    elif chose == "4":
        delete_student()

    elif chose == "5":
        update_student()

    elif chose == "6":
        delete_all_student()

    elif chose == "7":
        print("thanks for using our project")
        break
    else:
        print("\n ❌invalid choice")



