class ClassMethodDemo:
    institute = "" # class variable

    def addStudent(self,enrollmentNo,name,course):
        self.enrollmentNo = enrollmentNo
        self.name = name
        self.course = course

    def studentInfo(self):
        print("Student Information:",self.enrollmentNo,":",self.name,":",self.course)

    @classmethod
    def setInstituteName(cls):
        cls.institute = "IT-Vedant Education, Mumbai"

student1 = ClassMethodDemo()
student1.addStudent(10034,"Gargi Rout","Data Software Engineering")
student1.studentInfo()
ClassMethodDemo.setInstituteName()
student1.studentInfo()