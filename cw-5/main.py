file = "dataSets/studentsData.txt"
lines = open(file).readlines()
students = {}

for line in lines:
    split_student_data = line.strip().split(",")

    student_email = split_student_data[0]
    student_data = {
        "name": split_student_data[1],
        "surname": split_student_data[2],
        "points": float(split_student_data[3]),
        "grade": float(split_student_data[4]) if len(split_student_data) >= 5 else 0,
        "mailed": len(split_student_data) >= 6
    }

    students[student_email] = student_data


def calculate_grade(points):
    return points


for key in students:
    if students[key]["grade"] != 0:
        continue
    points = students[key]["points"]
    grade = calculate_grade(points)
    students[key]["grade"] = grade