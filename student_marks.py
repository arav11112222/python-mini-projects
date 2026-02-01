# Student Marks Management System - Beginner Python Project

def get_student_data():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_subjects):
        mark = float(input("Enter marks for subject:"))
        marks.append(mark)
    return name, marks

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage

def show_result(name, total, percentage):
    print("\nStudent Name:", name)
    print("Total Marks:",total)
    print("Percentage:",percentage)
    if percentage >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

# Main Program
while True:
    print("\n1. Enter Student Data")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name, marks = get_student_data()
        total, percentage = calculate_percentage(marks)
        show_result(name, total, percentage)
    elif choice == "2":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
