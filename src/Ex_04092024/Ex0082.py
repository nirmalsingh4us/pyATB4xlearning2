# take input and crate a class in python

class Person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Occupation is {self.occupation}")


# create an object
person1 = Person()
person1.name_of_the_function_to_display()
