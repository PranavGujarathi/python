class Father:
    def __init__(self):
        print("Father : ")

class Child(Father):
    def __init__(self):
        super().__init__()
        print("Child : ")


obj=Child()



