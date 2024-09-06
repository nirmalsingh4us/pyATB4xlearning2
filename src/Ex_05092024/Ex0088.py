class Car:

    def __init__(self,o_model,o_name,o_make):
        self.model = o_model
        self.name= o_name
        self.make = o_make

    def start_engine(self):
        print("Starting a car with name " + self.name)
        print("Starting a car with Model " + self.model)
        print("Starting a car with Make " + self.make)

Alto = Car ("2017","Alto k10","Maruti Suzuki")
Alto.start_engine()

print("----------")

i20 =  Car ("2015","i20","Hyundai")
i20.start_engine()