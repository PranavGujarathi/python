from abc import ABC, abstractmethod
class Help4Code(ABC):
    @abstractmethod
    def training(slef):
        pass

    @abstractmethod
    def placement(self):
        pass


class Ashish(Help4Code):
    def training(slef):
        print('c , c++, java')
    def placement(self):
        print('java placement')

class Niku(Help4Code):
    def training(slef):
        print('Python | Django')
    def placement(self):
        print('PYTHON placement')

class Diva(Help4Code):
    def training(slef):
        print('ML')
    def placement(self):
        print('Data placement')




obj1=Ashish()
obj1.training()
obj2=Niku()




