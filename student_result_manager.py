student = {}

while True:
    print("\n----- STUDENT MANAGER APP -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ").strip()

        try:
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Please enter valid numeric marks!")
            continue

        student[name] = marks
        print(f"{name} Successfully Added!")

    # View Students
    elif choice == "2":
        if len(student) == 0:
            print("No students found!")
        else:
            print("\nStudent List:")
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # Check Result
    elif choice == "3":
        name = input("Enter student name: ").strip()

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"{name} : PASS ({marks} Marks)")
            else:
                print(f"{name} : FAIL ({marks} Marks)")
        else:
            print("Student not found!")

    # Exit
    elif choice == "4":
        print("Exiting...")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please try again.")