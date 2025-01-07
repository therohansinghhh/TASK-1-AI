students = {}

def create_student(student_id, name, age, grades):
    if student_id in students:
        print("Student ID already exists. Try updating the student instead.")
    else:
        students[student_id] = {"name": name, "age": age, "grades": grades}
        print(f"Student {name} added successfully.")

def read_student(student_id):
    if student_id in students:
        print(f"Details for Student ID {student_id}:")
        print(f"Name: {students[student_id]['name']}")
        print(f"Age: {students[student_id]['age']}")
        print(f"Grades: {students[student_id]['grades']}")
    else:
        print("Student not found.")

def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = age
        if grades:
            students[student_id]['grades'] = grades
        print(f"Student ID {student_id} updated successfully.")
    else:
        print("Student not found.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Student not found.")

def display_all_students():
    if students:
        print("All Students:")
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grades: {details['grades']}")
    else:
        print("No students found.")

# Main program
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades = list(map(int, input("Enter Grades (comma-separated): ").split(',')))
            create_student(student_id, name, age, grades)
        
        elif choice == "2":
            student_id = input("Enter Student ID to view: ")
            read_student(student_id)
        
        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter New Name (or press Enter to skip): ")
            age = input("Enter New Age (or press Enter to skip): ")
            grades = input("Enter New Grades (comma-separated or press Enter to skip): ")
            update_student(student_id, name=name or None, 
                           age=int(age) if age else None, 
                           grades=list(map(int, grades.split(','))) if grades else None)
        
        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        
        elif choice == "5":
            display_all_students()
        
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
