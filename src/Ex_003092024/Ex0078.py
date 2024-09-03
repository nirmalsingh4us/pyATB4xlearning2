class Person:
# Attribute
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


# Behaviour
def talk(self):  # NRNAG # self -> this will be first agrument in every behaviour
    print("I can talk")

    def sleep(self, name):  # Arg with no return
        print("I am method!")

        print("sleep", name)

    def walk(self):
        print("I am walking")

    def walk_return(self):  # no Arg with return

        return "I am walking retun"
    # Create object of the class
    # objectref = classname() -> object


Nirmal = Person()
Nirmal.name = "Mr.Singh"
print(Nirmal.name)
Nirmal.talk()

Gurfateh = Person()
Gurfateh.age = 10
Gurfateh.name = "Gurfateh Singh"
Gurfateh.address = "Sultanwind Link road"
print(Gurfateh.age)
print(Gurfateh.name)
print(Gurfateh.address)

