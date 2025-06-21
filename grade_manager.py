import sqlite3

def create_table():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade REAL)              
                   ''')
    
    conn.commit()
    conn.close()

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)' , (name, grade))
    conn.commit()
    conn.close()
    print(f"Added {name} with the grade {grade}")


def view_student():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print("\nStudent Grades")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")
    conn.close()


def update_grade():
    name = input("Enter student grade to update: ")
    new_grade = float(input("Enter new grade: "))
    conn = sqlite3.connect("gades.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade,name))
    print(f"Updates {name}'s grade to {new_grade}")
    conn.commit()
    conn.close()

def delete_student():
    name = input("Enter student to delete: ")
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE name = ?', (name,))
    print(f"Deleted student {name}")
    conn.commit()
    conn.close()

def menu():
    create_table()
    while True:
        print("\n Student Grade Manager")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose an option:")


        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option Please try again")

menu()



    


