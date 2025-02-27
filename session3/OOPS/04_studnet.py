class Student:
    def __init__(self):
        self.name="Pranav"
        self.roll_no=19

    def getData(self):
        self.s_mb=123456789

obj=Student()
obj.getData()
obj.s_branch="IT"
print(obj.__dict__)
print(obj.s_mb)
del obj.roll_no
print(obj.__dict__)