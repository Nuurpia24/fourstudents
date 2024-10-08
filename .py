students = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30, "student_id": 11230, "grades": {"Python Programming 1": 1, "Database Technology": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32, "student_id": 11231, "grades": {"Python Programming 1": 1, "Python Programming 2": 3}},
    {"name": "Daniel Eliasson", "email": "daniel.eliasson@yh.nackademin.se", "age": 29, "student_id": 11233, "grades": {"Python Programming 1": 1, "Business Skills": 2}},
    {"name": "Magdalena Andersson", "email": "magdalena.andersson@yh.nackademin.se", "age": 50, "student_id": 11234, "grades": {"Python Programming 1": 1, "Web Frameworks in Python": 5}}
]

def list_students():
    print("\nList of all students:")
    for student in students:
        print(f"ID: {student['student_id']}, Name: {student['name']}, Age: {student['age']}, Email: {student['email']}")
        print("Grades:")
        for course, grade in student['grades'].items():
            print(f"  {course}: {grade}")
        print()

def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        email = input("Enter student's email address: ")
        grades = {}
           while True:
            course = input("Enter course name (or press Enter to finish): ")
            if not course:
                break
            grade = int(input(f"Enter grade for {course}: "))
            grades[course] = grade
        new_student = {
                    "name": name,
                    "email": email,
                    "age": age,
                    "student_id": student_id,
                    "grades": grades
                } 
       students.append(new_student)
        print(f"\nStudent {name} with ID {student_id} has been added.")
    except ValueError:
        print("Please enter a valid number for ID or age.") 
        def remove_student():
    try:
        student_id = int(input("Enter student ID of the student you want to remove: "))
        for student in students:
            if student['student_id'] == student_id:
                students.remove(student)
                print(f"\nStudent with ID {student_id} has been removed.")
                return
        print(f"\nNo student found with ID {student_id}.")
    except ValueError:
        print("Please enter a valid number for the student ID.")  

        def show_menu():
    print("\nChoose an option:")
    print("[q] Quit the program")
    print("[0] List all students with details")
    print("[1] Add a student")
    print("[2] Remove a student")      

    def main():
    print("Welcome to the student management system!")
    
    while True:
        show_menu()
        choice = input("Your choice: ").lower()
        
        if choice == 'q':
            print("Program is exiting. Goodbye!")
            break
        elif choice == '0':
            list_students()
        elif choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()