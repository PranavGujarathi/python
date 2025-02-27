#multilevel inheritance
class College:
      
    def college_name(self): 
        print("SCOE")

class Student(College): 

    def student_info(self): 

        print("Name: Pranav Gujarathi")
        print("Branch: IT")

class Exam(Student):
    def subject(self):
        print("Subject1: DBMS")
        print("Subject2: Math")

#multiple
class Submarks:
    math=int(input("Enter the marks"))
    dbms=int(input("Enter the marks"))
    aids=int(input("Enter the marks"))
    history=int(input("Enter the marks"))

class Practisemarks:
    cpract = int(input("Enter practise marks of aids: "))    


class Result(Submarks,Practisemarks):
    def total(self):
        if self.math >= 40 and self.dbms >= 40 and self.history >= 40 and self.cpract >= 20:
             print("pass")
        else:
            print("fail") 
obj = Result()
obj.total()

obj=Exam()
obj.college_name()
obj.student_info()

 