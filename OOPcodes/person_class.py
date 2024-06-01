# class Person:
#     def set_info(self,pid,pname,page): # self is used to refer to current object
#         self.pid = pid
#         self.pname = pname
#         self.page = page

# person1 = Person() # object
# person1.set_info(3,"Gargi Rout",22)
# print("ID:",person1.pid)
# print("Name:",person1.pname)
# print("Age:",person1.page)

# Create a class to represent student
# rollno, name, course, m1, m2, m3

class Student:
    def set_info(self,rollno,name,course,m1,m2,m3):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

student1 = Student()
student1.set_info(1,"Gargi Rout","Python",86,91,95)
print(student1.rollno,":",student1.name,":",student1.course,":",student1.m1,":",student1.m2,":",student1.m3)
total = student1.m1 + student1.m2 + student1.m3
avg = total // 3
print("Total Marks:",total)
print("Average Marks:",avg)

student2 = Student()
student2.set_info(2,"Misa Jarwal","Java",75,91,87)
print(student2.rollno,":",student2.name,":",student2.course,":",student2.m1,":",student2.m2,":",student2.m3)
total = student2.m1 + student2.m2 + student2.m3
avg = total // 3
print("Total Marks:",total)
print("Average Marks:",avg)