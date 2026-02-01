# Wellcome to our Smart student managment system
students_list = []
roll = 1


# add student
def add_student():
    global roll
    name = input("enter your name : ")
    marks1 = float(input("enter your Maths subject number : "))
    marks2 = float(input("enter your English subject number : "))
    marks3 = float(input("enter your Computer Science subject number : "))
    marks4 = float(input("enter your Urdu subject number : "))
    marks5 = float(input("enter your Statastic subject number : "))
    marks6 = float(input("enter your Islamyat subject number : "))
    marks7 = float(input("enter your Quran Hakeem subject number : "))

    student = {
        "roll": roll,
        "name": name,
        "marks": [marks1, marks2, marks3, marks4, marks5, marks6, marks7],
    }
    students_list.append(student)
    print("\nrecord sucessfull added")
    roll += 1
    return


# view student
def view_student():
    if not students_list:
        print("\n❌Student detailed not found❌")
        return
    for s in students_list:
        print("\n✔===Student record founds===✔")
        print(f"roll : {s["roll"]} | Name :  {s["name"]} | Marks : {s["marks"]}")


# search student
def search_student():
    if len(students_list) == 0:
        print("\n❌student not found❌")
        return
    roll = int(input("enter your roll to check : "))
    for s in students_list:
        if roll == s["roll"]:
            print("\n===Student found===")
            print(
                f"roll number : {s["roll"]} | Name :  {s["name"]} | Marks : {s["marks"]}"
            )
            return
    print("\n===result with roll number is not found===")


# caculate student
def caculate_student():
    if not students_list:
        print("\n no data to calculate result ")
        return
    print("\n===Result===")
    for s in students_list:
        total = sum(s["marks"])
        percentage = total / len(s["marks"])
        if percentage >= 80:
            grade = "A"
            status = "Pass"
        elif percentage >= 60:
            grade = "B"
            status = "Pass"
        elif percentage >= 40:
            grade = "C"
            status = "Pass"
        else:
            grade = "F"
            status = "Fail"

        print(f"Roll : {s["roll"]}")
        print(f"Name : {s["name"]}")
        print(f"Marks : {s["marks"]}")
        print(f"Total : {total}")
        print(f"Percentage : {percentage}")
        print(f"Grade : {grade}")
        print(f"Status : {status}")
        print("-" * 30)


# show topper
def show_topper():
    if not students_list:
        print("\n student not found ")
        return
    max_percentage = 0
    topper = None

    for student in students_list:
        total = sum(student["marks"])
        percentage = total / len(student["marks"])

        if percentage > max_percentage:
            max_percentage = percentage
            topper = student

    print("\n🏆 TOPPER 🏆")
    print("Roll no:", topper["roll"])
    print("Name :", topper["name"])
    print("Percentage :", max_percentage)


# delete student
def delete_student():
    if not students_list:
        print("\n===No student here to delete===")
        return
    roll = int(input("enter your roll number to delete student :"))
    for student in students_list:
        if student["roll"] == roll:
            students_list.remove(student)
            print("\n✔===Delete sucessfull===")
            break
    else:
        print("\n❌Roll number did'n match")
        return

    # re assign all value
    roll = 1
    for student in students_list:
        student["roll"] = roll
        roll += 1


# clear student
def clear_student():
    if not students_list:
        print("\nThere are no record here to delte")
        return
    students_list.clear()
    print("\n---clear sucessfull---")


# main
while True:
    print("\n===Wellcome to student result managment===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Show Topper")
    print("6. Delete student")
    print("7. Delete all")
    print("8. Exit")

    user_choice = input("Enter your choice : ")

    # condation
    if user_choice == "1":
        add_student()
    elif user_choice == "2":
        view_student()
    elif user_choice == "3":
        search_student()
    elif user_choice == "4":
        caculate_student()
    elif user_choice == "5":
        show_topper()
    elif user_choice == "6":
        delete_student()
    elif user_choice == "7":
        clear_student()
    elif user_choice == "8":
        print("Thank for using our project")
        break
    else:
        print("choose between 1 to 8")
        print("Are you blind")

