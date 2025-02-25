from sqlalchemy import Null


myStudents = []

def addStudent(id,name, rollNo, address, major):
    student = [id,name,rollNo,address,major]
    myStudents.append(student)
    return student


def updateStudentById(rollNo):
    try:
        for student in myStudents:
            if student[2] == rollNo:
                student[1] = name
                student[0] = id
                student[3] = address
                student[4] = major
                return student
    except:
        print("Student of id: " + id + " is not there!")

def updateStudent(name, rollNo, address, major):
    for student in myStudents:
        if student[2] == rollNo:
            student[1] = name
            student[2] = rollNo
            student[3] = address
            student[4] = major
            return student
        
def gatAllStudents():
    for student in myStudents:
        print(student)

def deleteStudent(id):
    try:
        for student in myStudents:
            if student[1] == id:
                myStudents.remove(student)
    except:
        print("Student of id: " + id + " is not there!")


while(True):
    print("1. Add Student")
    print("2. Get All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        ID = input("Enter ID: ")
        name = input("Enter Name: ")
        rollNo = int(input("Enter rollNo: "))
        address = input("Enter address: ")
        major = input("Enter major: ")
        addStudent(ID, name, rollNo, address, major)
        print(gatAllStudents())
    elif choice == 2:
        print(gatAllStudents())
    elif choice == 3:
        rollNo = int(input("Enter rollNo: "))
        student = updateStudentById(rollNo)
        if student is not None:
            student[1] = input("Enter Name: ")
            student[2] = input("Enter roll No: ")
            student[3] = input("Enter address: ")
            student[4] = input("Enter major: ")
            updateStudent(name, rollNo, address, major)
            print(gatAllStudents())
        else:
            print("Message: Student Not Found!")
    elif choice == 4:
        id = int(input("Enter id: "))
        deleteStudent(id)
        print(gatAllStudents())
    elif choice == 5:
        break
    else:
        print("Invalid choice")

