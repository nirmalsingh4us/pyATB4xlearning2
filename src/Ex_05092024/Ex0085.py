a = 10

class  Person:
    b = 11 # instance varibale -> to class

    def print_info(self):
        global a # Declare it as glboal
        a = "Hello Nirmal Singh"
        print(self.b)

obj_ref = Person()
obj_ref.print_info()
print(a)