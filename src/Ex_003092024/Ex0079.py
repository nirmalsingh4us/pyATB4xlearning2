class Dog:
    # A
    name = None
    breed = None
    color = None
    # B


def __init__(self, name, breed):


    print("called,object is created")
    self.name = name
    self.breed = breed


def sleep(self):
    print("Sleeping", self.name)


def bark(self):
    print("Bark")


def eat(self, food):
    print("Pedigree")


# Object reference

dog1 = Dog
print(dog1.name)
dog1.name = "Tyson"
dog1.sleep()
"""
print("------------------")
dog2 = Dog
print(dog1.name)
dog2.name ="Max"
dog2.bark()
dog2.eat()

print("------------------")
dog3 = Dog
print(dog3.name)
dog3.name ="Zoobi"
dog3.bark()
dog3.eat()
"""
