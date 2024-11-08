import random

def read_student_ids(path):
    with open(path, 'r') as file:
        student_ids = file.read().splitlines()
    return student_ids


def viva_selection(path):
    
    all_students = read_student_ids(path)
    students_left = all_students.copy()

    while students_left:
        
        selected_student = random.choice(students_left)
        print(f"Selected student for viva: {selected_student}")

        students_left.remove(selected_student)

    print("\nAll students have been selected. Reset the list.")

path = 'student.txt'  
viva_selection(path)