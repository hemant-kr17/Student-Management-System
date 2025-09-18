# main.py
from management import Management

def main():
    m = Management()
    m.load_student()

    while True:
        print("\nChoose One!!")
        print("1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            m.add_student()
        elif choice == "2":
            m.display_student()
        elif choice == "3":
            m.search_student()
        elif choice == "4":
            m.update_student()
        elif choice == "5":
            m.delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
