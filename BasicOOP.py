class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        if len(self.grades) > 0:
            average = sum(self.grades) / len(self.grades)
            print(f"Average Grade: {average:.2f}")
        else:
            print("No grades available to calculate the average.")

student1 = Student("Rohan", 19, [85, 88, 90])
student2 = Student("Adarsh", 19, [78, 82, 80])

print("Student 1 Details:")
student1.display_details()
student1.calculate_average()

print("\nStudent 2 Details:")
student2.display_details()
student2.calculate_average()
