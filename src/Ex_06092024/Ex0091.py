# encapsulation
# Can bind the data variable with the mehtods
# Data member -/ class variable
# methods - def function within the class
# wrapping or binding the data variables with the method - encapsulation

class Car:
    model = None
    name = None
    Password = "abc123"

    def __init__(self):
        self.password = "Nirmal"

    def change_pwd(self):
        print(self.password)

obj_ref = Car()
print(obj_ref.password)

obj_ref.change_pwd()

