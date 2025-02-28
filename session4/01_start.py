class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Pranav", 19)
print(p1.name, p1.age)
print(f"person1 is an object with name {p1.name} and age is {p1.age}")
p1.intro()




class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id): 
        super().__init__(name, age) 
        self.student_id = student_id 

    def introduce(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}, with ID {self.student_id}")
    
    @staticmethod
    def validate_student_id(student_id):
        return isinstance(student_id, str) and student_id.isdigit() and len(student_id) > 0  

# Example usage
s1 = Student("Pranav", 19, "12345")
s1.introduce()

# Validate student ID
print(Student.validate_student_id("12345"))  
print(Student.validate_student_id("abc12"))  
