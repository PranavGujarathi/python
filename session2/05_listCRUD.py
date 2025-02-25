import sys

class CRUD:
    def __init__(self):
        print("Student Management System ")
        self.studentID=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]

    def addStudent(self,id,name,no,city):
        self.studentID.append(id)
        self.studentName.append(name)
        self.studentRollNo.append(no)
        self.studentCity.append(city)

    def showData(self):
        if not self.studentID:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for i in range(len(self.studentID)):
                print(f"ID: {self.studentID[i]}, Name: {self.studentName[i]}, Roll No: {self.studentRollNo[i]}, City: {self.studentCity[i]}")


crud = CRUD()
crud.addStudent(1, "Pranav", "19", "Bhiwandi")
crud.showData()
