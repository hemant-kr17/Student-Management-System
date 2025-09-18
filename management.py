# management.py
from student import Student

class Management:
    def __init__(self):
        self.list_of_student = []

    # Load students from file
    def load_student(self):
        try:
            with open('student_data.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:
                        name, age, roll_no, grade, percentage = data
                        student = Student(name, int(age), int(roll_no), int(grade), float(percentage))
                        self.list_of_student.append(student)
            print("Student Loaded Successfully From File!!")
        except FileNotFoundError:
            print("No file found, Start adding students first.")

    # Add student
    def add_student(self):
        while True:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            roll_no = int(input("Enter your roll number: "))
            grade = int(input("Enter your grade: "))
            percentage = float(input("Enter your percentage: "))

            s = Student(name, age, roll_no, grade, percentage)
            self.list_of_student.append(s)
            print("Student added successfully!\n")

            choice = input("Do you want to add another? (y/n): ")
            if choice.lower() != 'y':
                break

        # Save all students to file
        with open('student_data.txt', 'w') as file:
            for student in self.list_of_student:
                file.write(f"{student.name},{student.age},{student.roll_no},{student._grade},{student._Student__percentage}\n")

    # Display all students
    def display_student(self):
        try:
            with open('student_data.txt', 'r') as f:
                content = f.read()
                print("Student Records:\n", content)
        except FileNotFoundError:
            print("No student records found!")

    # Search student
    def search_student(self):
        option = input("Search by Name/Roll/Grade: ").lower()
        if option == 'name':
            value = input("Enter Student Name: ")
        elif option == 'roll':
            value = int(input("Enter Roll: "))
        elif option == 'grade':
            value = int(input("Enter Grade: "))
        else:
            print("Invalid option!")
            return

        found = False
        for student in self.list_of_student:
            if (option == 'name' and student.name.lower() == value.lower()) or \
               (option == 'roll' and student.roll_no == value) or \
               (option == 'grade' and student._grade == value):
                print(student.get_details())
                found = True

        if not found:
            print("No student found with this information!")

    # Update student
    def update_student(self):
        option = input("Update by Name or Roll Number? ").lower()
        found = False

        if option == 'name':
            name = input("Enter Name: ")
            for student in self.list_of_student:
                if student.name.lower() == name.lower():
                    found = True
                    print(student.get_details())
                    while True:
                        print("\nSelect field to update:")
                        print("1. Name\n2. Age\n3. Roll Number\n4. Grade\n5. Percentage\n6. Exit")
                        choice = input("Enter your choice: ")

                        if choice == '1':
                            student.name = input("Enter new Name: ")
                        elif choice == '2':
                            student.age = int(input("Enter new Age: "))
                        elif choice == '3':
                            student.roll_no = int(input("Enter new Roll Number: "))
                        elif choice == '4':
                            student._grade = int(input("Enter new Grade: "))
                        elif choice == '5':
                            student.percentage = float(input("Enter new Percentage: "))
                        elif choice == '6':
                            break
                        else:
                            print("Invalid choice!")

        elif option == 'roll number':
            roll = int(input("Enter Roll Number: "))
            for student in self.list_of_student:
                if student.roll_no == roll:
                    found = True
                    print(student.get_details())
                    while True:
                        print("\nSelect field to update:")
                        print("1. Name\n2. Age\n3. Roll Number\n4. Grade\n5. Percentage\n6. Exit")
                        choice = input("Enter your choice: ")

                        if choice == '1':
                            student.name = input("Enter new Name: ")
                        elif choice == '2':
                            student.age = int(input("Enter new Age: "))
                        elif choice == '3':
                            student.roll_no = int(input("Enter new Roll Number: "))
                        elif choice == '4':
                            student._grade = int(input("Enter new Grade: "))
                        elif choice == '5':
                            student.percentage = float(input("Enter new Percentage: "))
                        elif choice == '6':
                            break
                        else:
                            print("Invalid choice!")

        else:
            print("Invalid Choice!")
            return

        if found:
            # Save updated list to file
            with open('student_data.txt', 'w') as file:
                for student in self.list_of_student:
                    file.write(f"{student.name},{student.age},{student.roll_no},{student._grade},{student._Student__percentage}\n")
            print("Student Updated Successfully!")
        else:
            print("No student found with this information!")

    # Delete student
    def delete_student(self):
        option = input("Delete by Name or Roll Number? ").lower()
        found = False

        if option == 'name':
            name = input("Enter Name: ")
            for student in self.list_of_student:
                if student.name.lower() == name.lower():
                    print(f"Deleting: {student.get_details()}")
                    self.list_of_student.remove(student)
                    found = True
                    break

        elif option == 'roll number':
            roll = int(input("Enter Roll Number: "))
            for student in self.list_of_student:
                if student.roll_no == roll:
                    print(f"Deleting: {student.get_details()}")
                    self.list_of_student.remove(student)
                    found = True
                    break

        else:
            print("Invalid Choice!")
            return

        if found:
            # Rewrite the file
            with open('student_data.txt', 'w') as file:
                for student in self.list_of_student:
                    file.write(f"{student.name},{student.age},{student.roll_no},{student._grade},{student._Student__percentage}\n")
            print("Student deleted successfully!")
        else:
            print("No student found with this information!")
