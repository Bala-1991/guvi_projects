import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Secret007!',  # Your MySQL password
            database='school_dbms'  # Your database name
        )
        if connection.is_connected():
            print("Connected to MySQL Database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# User Authentication for Admin
def authenticate_admin(connection):
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM admin WHERE user_name = %s AND password = %s', (username, password))
    return cursor.fetchone() is not None

# View Students
def view_students(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM student')
    for row in cursor.fetchall():
        print(row)

# View Teachers
def view_teachers(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM teacher')
    for row in cursor.fetchall():
        print(row)

# View Principals
def view_principals(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM principal')
    for row in cursor.fetchall():
        print(row)

# Manage Students (Admin only)
def manage_students(connection):
    cursor = connection.cursor()
    while True:
        print("\nManage Students")
        print("1. Add Student\n2. Update Student\n3. Delete Student\n4. View Students\n5. Back")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                name = input("Name: ")
                age = int(input("Age: "))
                sex = input("Sex (Male/Female/Other): ")
                class_ = input("Class: ")
                fees = float(input("Fees: "))
                rank = int(input("Rank: "))
                english_mark = int(input("English Mark: "))
                python_mark = int(input("Python Mark: "))
                math_mark = int(input("Math Mark: "))
                class_teacher = input("Class Teacher: ")
                
                cursor.execute('''
                INSERT INTO student (name, age, sex, class, fees, `rank`, english_mark, python_mark, math_mark, class_teacher)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (name, age, sex, class_, fees, rank, english_mark, python_mark, math_mark, class_teacher))
                connection.commit()
                print("Student added.")
            except Exception as e:
                print(f"Error adding student: {e}")

        elif choice == '2':
            try:
                sno = int(input("Enter Student SNO to update: "))
                name = input("New Name (leave blank for no change): ")
                if name == "":
                    name = None
                age = input("New Age (leave blank for no change): ")
                if age == "":
                    age = None
                else:
                    age = int(age)
                sex = input("New Sex (leave blank for no change): ")
                if sex == "":
                    sex = None
                class_ = input("New Class (leave blank for no change): ")
                if class_ == "":
                    class_ = None
                fees = input("New Fees (leave blank for no change): ")
                if fees == "":
                    fees = None
                else:
                    fees = float(fees)
                rank = input("New Rank (leave blank for no change): ")
                if rank == "":
                    rank = None
                else:
                    rank = int(rank)

                cursor.execute('''
                UPDATE student SET
                    name = COALESCE(%s, name),
                    age = COALESCE(%s, age),
                    sex = COALESCE(%s, sex),
                    class = COALESCE(%s, class),
                    fees = COALESCE(%s, fees),
                    `rank` = COALESCE(%s, `rank`)
                WHERE sno = %s
                ''', (name, age, sex, class_, fees, rank, sno))
                connection.commit()
                print("Student updated.")
            except Exception as e:
                print(f"Error updating student: {e}")

        elif choice == '3':
            try:
                sno = int(input("Enter Student SNO to delete: "))
                cursor.execute('DELETE FROM student WHERE sno = %s', (sno,))
                connection.commit()
                print("Student deleted.")
            except Exception as e:
                print(f"Error deleting student: {e}")
        
        elif choice == '4':
            view_students(connection)

        elif choice == '5':
            break

# Manage Teachers (Admin only)
def manage_teachers(connection):
    cursor = connection.cursor()
    while True:
        print("\nManage Teachers")
        print("1. Add Teacher\n2. Update Teacher\n3. Delete Teacher\n4. View Teachers\n5. Back")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                name = input("Name: ")
                age = int(input("Age: "))
                sex = input("Sex (Male/Female/Other): ")
                salary = float(input("Salary: "))
                class_teacher_class = input("Class Teacher Class: ")
                
                cursor.execute('''
                INSERT INTO teacher (name, age, sex, salary, class_teacher_class)
                VALUES (%s, %s, %s, %s, %s)
                ''', (name, age, sex, salary, class_teacher_class))
                connection.commit()
                print("Teacher added.")
            except Exception as e:
                print(f"Error adding teacher: {e}")

        elif choice == '2':
            try:
                sno = int(input("Enter Teacher SNO to update: "))
                name = input("New Name (leave blank for no change): ")
                if name == "":
                    name = None
                age = input("New Age (leave blank for no change): ")
                if age == "":
                    age = None
                else:
                    age = int(age)
                sex = input("New Sex (leave blank for no change): ")
                if sex == "":
                    sex = None
                salary = input("New Salary (leave blank for no change): ")
                if salary == "":
                    salary = None
                else:
                    salary = float(salary)
                class_teacher_class = input("New Class Teacher Class (leave blank for no change): ")
                if class_teacher_class == "":
                    class_teacher_class = None

                cursor.execute('''
                UPDATE teacher SET
                    name = COALESCE(%s, name),
                    age = COALESCE(%s, age),
                    sex = COALESCE(%s, sex),
                    salary = COALESCE(%s, salary),
                    class_teacher_class = COALESCE(%s, class_teacher_class)
                WHERE sno = %s
                ''', (name, age, sex, salary, class_teacher_class, sno))
                connection.commit()
                print("Teacher updated.")
            except Exception as e:
                print(f"Error updating teacher: {e}")

        elif choice == '3':
            try:
                sno = int(input("Enter Teacher SNO to delete: "))
                cursor.execute('DELETE FROM teacher WHERE sno = %s', (sno,))
                connection.commit()
                print("Teacher deleted.")
            except Exception as e:
                print(f"Error deleting teacher: {e}")
        
        elif choice == '4':
            view_teachers(connection)

        elif choice == '5':
            break

# Manage Principals (Admin only)
def manage_principals(connection):
    cursor = connection.cursor()
    while True:
        print("\nManage Principals")
        print("1. Add Principal\n2. Update Principal\n3. Delete Principal\n4. View Principals\n5. Back")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                name = input("Name: ")
                age = int(input("Age: "))
                sex = input("Sex (Male/Female/Other): ")
                salary = float(input("Salary: "))
                
                cursor.execute('''
                INSERT INTO principal (name, age, sex, salary)
                VALUES (%s, %s, %s, %s)
                ''', (name, age, sex, salary))
                connection.commit()
                print("Principal added.")
            except Exception as e:
                print(f"Error adding principal: {e}")

        elif choice == '2':
            try:
                sno = int(input("Enter Principal SNO to update: "))
                name = input("New Name (leave blank for no change): ")
                if name == "":
                    name = None
                age = input("New Age (leave blank for no change): ")
                if age == "":
                    age = None
                else:
                    age = int(age)
                sex = input("New Sex (leave blank for no change): ")
                if sex == "":
                    sex = None
                salary = input("New Salary (leave blank for no change): ")
                if salary == "":
                    salary = None
                else:
                    salary = float(salary)

                cursor.execute('''
                UPDATE principal SET
                    name = COALESCE(%s, name),
                    age = COALESCE(%s, age),
                    sex = COALESCE(%s, sex),
                    salary = COALESCE(%s, salary)
                WHERE sno = %s
                ''', (name, age, sex, salary, sno))
                connection.commit()
                print("Principal updated.")
            except Exception as e:
                print(f"Error updating principal: {e}")

        elif choice == '3':
            try:
                sno = int(input("Enter Principal SNO to delete: "))
                cursor.execute('DELETE FROM principal WHERE sno = %s', (sno,))
                connection.commit()
                print("Principal deleted.")
            except Exception as e:
                print(f"Error deleting principal: {e}")
        
        elif choice == '4':
            view_principals(connection)

        elif choice == '5':
            break

# Main Menu
def main_menu(connection):
    while True:
        print("\n--- School DBMS ---")
        print("1. Admin Login")
        print("2. View Students")
        print("3. View Teachers")
        print("4. View Principals")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            if authenticate_admin(connection):
                print("Authenticated as Admin.")
                while True:
                    print("\nAdmin Menu")
                    print("1. Manage Students")
                    print("2. Manage Teachers")
                    print("3. Manage Principals")
                    print("4. Logout")
                    
                    admin_choice = input("Choose an option: ")
                    
                    if admin_choice == '1':
                        manage_students(connection)
                    elif admin_choice == '2':
                        manage_teachers(connection)
                    elif admin_choice == '3':
                        manage_principals(connection)
                    elif admin_choice == '4':
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid admin credentials.")
        
        elif choice == '2':
            view_students(connection)
        elif choice == '3':
            view_teachers(connection)
        elif choice == '4':
            view_principals(connection)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# Setup
connection = create_connection()
if connection:
    main_menu(connection)
    # Close the connection
    connection.close()
