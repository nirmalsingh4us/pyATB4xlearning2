from abc import ABC, abstractmethod
class PyATB(ABC):
    @abstractmethod
    def payfee(self):
        pass
    def enrolled(self):
        print("Enrolled")

class Nirmal(PyATB):

    def payfee(self):
        print("Already paid the fee")

ob = Nirmal()
ob.payfee()