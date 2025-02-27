# Single level inheritance

class College:  #parent class
    def collegename(self): # member function of college
        print("Modern College")

class Student(College): # child class
    def studentinfo(self): # nemeber function
        print("Name: Pranav Gujarathi")
        print("Branch: IT")
     


obj = Student()# object create child class

obj.collegename()

obj.studentinfo()