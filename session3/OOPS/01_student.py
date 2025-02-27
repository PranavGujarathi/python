class Student:
    roll_no=19
    num1=50
    num2=100

    def add(self):
        print(self.num1+self.num2)
        self.name = input("Enter name : ")
        print(self.name)

obj=Student()
obj.add()
print(obj.roll_no)

