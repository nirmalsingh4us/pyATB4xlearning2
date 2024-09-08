from abc import ABC, abstractmethod
class Father(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    pass
   # def loan(self):
    #    print("son will be pay the loan")

son_obj = Son("1lac")
son_obj.loan()
