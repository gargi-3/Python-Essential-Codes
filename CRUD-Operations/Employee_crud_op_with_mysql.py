import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="batch413db")

def add_employee():
    id = input("Enter value for id : ")
    name = input("Enter value for name : ")
    job = input("Enter value for job : ")
    sal = input("Enter value for salary : ")
    email = input("Enter value for email : ")
    data = (id, name, job, sal, email)
    
    query = "insert into employee413 values(%s, %s, %s, %s, %s)"
    c = con.cursor()
    c.execute(query, data)
    con.commit()

    print("Employee added successfully...")
    menu()

def remove_employee():
    id = input("Enter the id of employee to remove : ")
    c = con.cursor()

    query = "delete from employee413 where id = %s"
    data = (id,)

    c.execute(query, data)
    con.commit()

    print("Employee record deleted successfully...")
    menu()

def update_employee():
    id = input("Enter the id of employee to update : ")
    c = con.cursor()

    query = "update employee413 set name=%s, job=%s, sal=%s, email=%s where id = %s"
    newName = input("Enter new name : ")
    newJob = input("Enter new job : ")
    newSal = input("Enter new salary : ")
    newEmail = input("Enter new email : ")

    data = (newName, newJob, newSal, newEmail, id)

    c.execute(query, data)
    con.commit()

    print("Eployee updated successfully...")
    menu()

def display_employees():
    c = con.cursor()

    query = "select * from employee413"
    c.execute(query)

    result = c.fetchall()
    for record in result:
        print("Employee info -> [Id : ", record[0], ", Name : ", record[1], ", Job : ", record[2], ", Salary : ", record[3], ", Email Id : ", record[4], "]")

    menu()

def menu():
    print("****** Employee Management CRUD Demo ****** ")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Display Employee")
    print("5. Exit")

    choice = int(input("Enter value for choice : "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_employee()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        display_employees()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid choice")
        menu()

menu()