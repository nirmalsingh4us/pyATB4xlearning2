from abc import ABC, abstractmethod
class Gearbox(ABC):
    @abstractmethod
    def Gearbox(self):
        pass
class Engine(ABC):
    @abstractmethod
    def start(self):
          pass
    @abstractmethod
    def stop(self):
        pass

class Car(Engine):
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")
    def Gearbox(self):
        print("change the Gear and drive the car slowly")
    def Drive(self):
        self.start()
        self.Gearbox()
        self.stop()


car = Car()
car.Drive()
