class Person:
# class variable
# Instance variable
    #name = "Nirmal" # if varialbe mention in the class it become hardcode

    def __init__(self,name): # Constructor is basically use to change the instance variable value
        self.name = name
    def walk(self, name):
        self.name = name
        print(self.name)

    def sing(self):
        return self.name



amit = Person("Amit")
nirmal = Person("Nirmal")
print(amit.name)
print(nirmal.name)
print("Who is singing the song ->",nirmal.sing())