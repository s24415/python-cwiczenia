def parse_students_from_file(file_path):
    result = {}
    data_lines = open(file_path).readlines()
    for line in data_lines:
        split_student_data = line.strip().split(",")

        student_email = split_student_data[0]
        student_data = {
            "name": split_student_data[1],
            "surname": split_student_data[2],
            "points": int(split_student_data[3]),
            "grade": float(split_student_data[4]) if len(split_student_data) >= 5 else 0,
            "mailed": len(split_student_data) >= 6
        }

        result[student_email] = student_data

    return result


def calculate_grade(points):
    if points <= 50:
        return 2
    elif points <= 60:
        return 3
    elif points <= 70:
        return 3.5
    elif points <= 80:
        return 4
    elif points <= 90:
        return 4.5

    return 5


def calculate_grades(students_dict):
    for key in students_dict:
        if students_dict[key]["grade"] != 0:
            continue
        points = students_dict[key]["points"]
        grade = calculate_grade(points)
        students_dict[key]["grade"] = grade


def save_students_data(students_dict, file_path):
    file = open(file_path, "w")
    for key in students_dict:
        file.write(f"{key},{students_dict[key]['name']},"
                   f"{students_dict[key]['surname']},{students_dict[key]['points']},"
                   f"{students_dict[key]['grade']}, {'MAILED' if students_dict[key]['mailed'] else ''}\n")


def add_new_student(students_dict):
    email = input("E-mail: ")
    if email in students_dict:
        print("Student with given E-mail already exists")
        return
    name = input("Name: ")
    surname = input("Surname: ")
    points = int(input("Points: "))
    students_dict[email] = {
        "name": name,
        "surname": surname,
        "points": points,
        "grade": calculate_grade(points),
        "mailed": False
    }


def delete_student(students_dict):
    for key in students_dict:
        print(f"{key} | {students_dict[key]}")

    removed_student_email = input("Insert E-mail of student: ")
    del students_dict[removed_student_email]


def mail_all_students(students_dict):
    return ""


data_set_path = "dataSets/studentsData.txt"
students = parse_students_from_file(data_set_path)

while True:
    print("1. ADD NEW STUDENT")
    print("2. REMOVE STUDENT")
    print("3. CALCULATE STUDENT'S GRADES")
    print("4. MAIL ALL STUDENTS")

    user_choice = int(input("Choice: "))

    if user_choice == 1:
        add_new_student(students)
        save_students_data(students, data_set_path)
    elif user_choice == 2:
        delete_student(students)
        save_students_data(students, data_set_path)
    elif user_choice == 3:
        calculate_grades(students)
        save_students_data(students, data_set_path)
    elif user_choice == 4:
        mail_all_students(students)
        save_students_data(students, data_set_path)
    else:
        print("Invalid option")
