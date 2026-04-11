
class Student:
    def __init__(self, name, grade, favorite_subject):
        self.name = name
        self.grade = grade
        self.favorite_subject = favorite_subject

    def get_data(self):
        return f"{self.name},{self.grade},{self.favorite_subject}\n"


def add_student(file_name):
    name = input("Enter student name: ")
    grade = input("Enter class/grade: ")
    fav_sub = input("Enter favorite subject: ")

    student = Student(name, grade, fav_sub)

    with open(file_name, "a") as file:  
        file.write(student.get_data())

    print(" Student added successfully!\n")



def view_students(file_name):
    try:
        with open(file_name, "r") as file:
            print("\n Student Records:")
            print(file.read())
    except FileNotFoundError:
        print(" File not found!\n")



def overwrite_students(file_name):
    print(" This will erase all existing data!")
    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "yes":
        with open(file_name, "w") as file:  
            n = int(input("How many students to enter? "))

            for i in range(n):
                print(f"\nEnter details for student {i+1}")
                name = input("Name: ")
                grade = input("Grade: ")
                fav_sub = input("Favorite Subject: ")

                student = Student(name, grade, fav_sub)
                file.write(student.get_data())

        print(" File overwritten successfully!\n")
    else:
        print(" Operation cancelled.\n")


file_name = "students.txt"

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Overwrite File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(file_name)
    elif choice == "2":
        view_students(file_name)
    elif choice == "3":
        overwrite_students(file_name)
    elif choice == "4":
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice! Try again.\n")