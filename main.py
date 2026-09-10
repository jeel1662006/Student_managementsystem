"""
# File name where student data will be stored
FILE_NAME = "students.txt"


# Add Student
def add_student(name, marks):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{marks}\n")

    print(f"{name} is added with marks {marks}")


# Display All Students
def display_student():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if students:
            print("\n--- Student Details ---")

            for student in students:
                name, marks = student.strip().split(",")
                print(f"{name} = {marks}")

        else:
            print("No student found.")

    except FileNotFoundError:
        print("No student found.")


# Update Student
def update_student(name, marks):
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for student in students:
                old_name, old_marks = student.strip().split(",")

                if old_name == name:
                    file.write(f"{name},{marks}\n")
                    found = True
                else:
                    file.write(student)

        if found:
            print(f"{name} is updated with marks {marks}")
        else:
            print(f"{name} is not found.")

    except FileNotFoundError:
        print(f"{name} is not found.")


# Delete Student
def delete_student(name):
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for student in students:
                old_name, old_marks = student.strip().split(",")

                if old_name == name:
                    found = True
                else:
                    file.write(student)

        if found:
            print(f"{name} has been deleted.")
        else:
            print(f"{name} is not found.")

    except FileNotFoundError:
        print(f"{name} is not found.")


# Main Function
def main():

    while True:

        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            name = input("Enter the student name: ")
            marks = int(input(f"Enter the marks of {name}: "))

            add_student(name, marks)

        elif choice == 2:

            name = input("Enter the student name: ")
            marks = int(input(f"Enter the updated marks of {name}: "))

            update_student(name, marks)

        elif choice == 3:

            name = input("Enter the student name: ")

            delete_student(name)

        elif choice == 4:

            display_student()

        elif choice == 5:

            print("Thank you for using Student Management System.")
            break

        else:

            print("Invalid Input")


# Start Program
if __name__ == "__main__":
    main()


"""

class Student:
    def __init__(self,name, marks, attendance):
        self.name= name
        self.marks= marks
        self.attendance = attendance


    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1= Student("Jeel", 90, 45)
s2 = Student("Jems",56,89)

print(s1.calculate_grade())

