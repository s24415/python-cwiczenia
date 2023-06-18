import tkinter as tk
import sqlite3
from tkinter import messagebox


class Student:
    def __init__(self, name, surname, email, points, grade):
        self.name = name
        self.surname = surname
        self.email = email
        self.points = points
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nEmail: {self.email}\nPoints: {self.points}\nGrade: {self.grade}"


class StudentDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS students (name TEXT, surname TEXT, email TEXT, points INTEGER, grade TEXT)"
        )
        self.conn.commit()

    def add_student(self, student):
        try:
            self.cursor.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                (student.name, student.surname, student.email, student.points, student.grade),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def delete_student(self, email):
        try:
            self.cursor.execute(
                "DELETE FROM students WHERE email=?", email
            )
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def update_student(self, updated_data):
        try:
            self.cursor.execute(
                "UPDATE students SET name=?, surname=?, points=?, grade=? WHERE email=?",
                (updated_data.name, updated_data.surname, updated_data.points, updated_data.grade, updated_data.email),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def get_all_students(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            rows = self.cursor.fetchall()
            students = []
            for row in rows:
                student = Student(row[0], row[1], row[2], row[3], row[4])
                students.append(student)
            return students
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.db = StudentDatabase("students.db")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.surname_label = tk.Label(root, text="Surname")
        self.surname_label.pack()
        self.surname_entry = tk.Entry(root)
        self.surname_entry.pack()

        self.email_label = tk.Label(root, text="Email")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.points_label = tk.Label(root, text="Points")
        self.points_label.pack()
        self.points_entry = tk.Entry(root)
        self.points_entry.pack()

        self.grade_label = tk.Label(root, text="Grade")
        self.grade_label.pack()
        self.grade_entry = tk.Entry(root)
        self.grade_entry.pack()

        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)


def handleAdd():
    student = Student(
        name_entry.get(),
        surname_entry.get(),
        email_entry.get(),
        points_entry.get(),
        grade_entry.get()
    )
    student_repository.add_student(student)


def handleDisplay():
    student_list = student_repository.get_all_students()
    messagebox.showinfo("Students", student_list)


def handleDelete():
    student_repository.delete_student(delete_entry.get())


def handleEdit():
    student_data = Student(
        name_entry.get(),
        surname_entry.get(),
        email_entry.get(),
        points_entry.get(),
        grade_entry.get()
    )
    student_repository.update_student(student_data)


student_repository = StudentDatabase("StudentDB")

root = tk.Tk()
root.title("Book Store")
root.geometry("800x500")

screen_width = 800
screen_height = 500

name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

surname_label = tk.Label(root, text="Surname")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

email_label = tk.Label(root, text="Email")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

points_label = tk.Label(root, text="Points")
points_label.pack()
points_entry = tk.Entry(root)
points_entry.pack()

grade_label = tk.Label(root, text="Grade")
grade_label.pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

add_button = tk.Button(root, text="Add Student", command=handleAdd)
add_button.pack()

display_button = tk.Button(root, text="Display Students", command=handleDisplay)
display_button.pack()

edit_button = tk.Button(root, text="Edit Student", command=handleEdit)
edit_button.pack()

delete_entry = tk.Entry(root)
delete_entry.pack()

delete_button = tk.Button(root, text="Delete Student", command=handleDelete)
delete_button.pack()

root.mainloop()
