empty_dict = {}
print("empty_dict:",empty_dict,type(empty_dict))

employee = {"ename":"Gargi","age":22,"email":"gargi.zr25@gmail.com",
            "city":"Panvel","dept":"Student","salary":1000,"company":"Itvedant"}
print(employee)

print("Name:",employee["ename"],"Email:",employee["email"])
print("City:",employee.get("city"),"Dept:",employee.get("dept"))

# adding elements to dictionary one at a time
student = {}
print("Student:",student)
student[1] = "Peter"
student[2] = "Ralph"
student[3] = "Ricky"
student[4] = "Joseph"

print("Student dictionary:",student)

# updating an element of dictionary
name = "Vicky"
student[3] = name
print("Updated student dictionary:",student)
