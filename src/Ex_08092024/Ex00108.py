# Abstraction : Hiding the details and show what is required.

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    #def sound(self):
        pass
    #    print("Bark")

ss = Dog("tyson")
ss.sound()