# This code will give error because method overloading is not supported in python
'''
class Arithmatic:
    def add(self,a):
        print(a)
    def add(selfa,b):
        print(a+b)
    def add(a,b,c):
        print(a+b+c)
obj = Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)
'''


#To handle overloaded method in python
#if method with variable number of arguements required then we can handle with default parameeters
'''
class Arithmatic:
    def add(self,a=None,b= None, c= None):
        if a!= None and b!=None:
          print(a+b)
        elif a!= None and b!=None and c!= None:
            print(a+b+c)
        else:
            print("Enter the last three arguements: ")
obj = Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)
'''


# Constructor overloading  ( python dont support )
'''class Arith:
    def __init__(self):
        print("There is no arguement")
    def _init_(self,a):
        print("passing one arguement")
    def _init_(self,a,b):
        print("passing two arguement")

obj = Arith()
obj = Arith(10)
obj = Arith(2,2)

'''



