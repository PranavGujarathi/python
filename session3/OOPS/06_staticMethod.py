# static method 

class Student:
    #by ussing class name we can acceess static method
    @staticmethod
    def get_details(fName,LName):
        print("Your details : ", fName,LName)

    @staticmethod
    def contact_detail(mobileNo,rollNo):
        print("Your contact number is : " , mobileNo ,rollNo)

Student.get_details("Pranav", "Gujarathi")
Student.contact_detail(123456789,19)

