# 🎓 Smart Student Management System (Console Based)

A Python **console-based student management system** to manage students, their marks, and results.  
Perfect for learning **lists, dictionaries, loops, and functions** in Python.  

---

## ✨ Features

- 📝 Add new students with marks for **7 subjects**  
- 👀 View all student records  
- 🔍 Search for a student by **roll number**  
- 📊 Calculate **total marks, percentage, grade, and pass/fail**  
- 🏆 Display the **topper** (highest percentage)  
- 🗑️ Delete a **specific student** by roll number  
- 🧹 Clear **all student records**  
- 🔢 Automatic **roll number assignment** with re-sequencing after deletion  

---

## 🌟 Special Highlights

- **Auto Roll Number:** Each student gets a **unique roll number automatically**. Roll numbers are **re-assigned sequentially** after deleting a student.  
- **Safe Delete Function:** Delete **any student** by roll number without breaking the list.  
- **Grade Calculation:** Automatically calculates grades based on percentage:  
  - `>= 80%` → **A**  
  - `>= 60%` → **B**  
  - `>= 40%` → **C**  
  - `< 40%` → **Fail**  
- **Topper Function:** Shows the student with the **highest percentage** automatically.  
- **Professional Console Interface:** Clean menu, sequential rolls, and proper formatting for easy use.  

---

## 🚀 How to Use

1. **Run the program** in Python 3.x:
   ```bash
   python student_management.py



2.Choose an option from the menu:

1️⃣ Add Student
2️⃣ View All Students
3️⃣ Search Student
4️⃣ Calculate Result
5️⃣ Show Topper
6️⃣ Delete Student
7️⃣ Delete All
8️⃣ Exit


Add a Student: Enter name and marks for 7 subjects. Roll number is assigned automatically.

View All Students: Displays all records in a clean format.
example:
	Roll: 3 | Name: Ali | Marks: [90, 85, 80, 75, 88, 92, 95]

Search Student: Enter roll number to find a specific student.
Example:
	Enter roll to check: 3
	Roll: 3 | Name: Ali | Marks: [90, 85, 80, 75, 88, 92, 95]


Calculate Result: Displays total, percentage, grade, and pass/fail for all students.
example:
	===Result===
	Roll : 1
	Name : ali
	Marks : [55.0, 55.0, 44.0, 55.0, 67.0, 56.0, 44.0]
	Total : 376.0
	Percentage : 53.714285714285715
	Grade : C
	Status : Pass

Show Topper: Displays the student with the highest percentage.
example:
	🏆 TOPPER 🏆
	Roll no: 1
	Name : ali
	Percentage : 53.714285714285715

Delete Student: Enter a roll number to delete a student. Remaining students’ roll numbers are re-sequenced automatically.
example:
	enter your roll number to delete student :1

	===Delete sucessfull===

Delete All: Clears all student records.
example:
	---clear sucessfull---

🔟 Exit: Close the program.
	😇Thank for using our project😇



🛠 Requirements

Python 3.x

No external libraries required

🔹 Why This Project Is Special

Uses Python fundamentals effectively (lists, dictionaries, loops, conditionals, functions).

Handles edge cases, like deleting students from the middle of the list, without breaking the program.

Auto-updates roll numbers and maintains sequence automatically.

Simple console interface for learning and testing basic Python programming skills.


🔹 Author

Developed by [Munazir abbas]
A learning-focused project to strengthen Python skills and understanding of data structures