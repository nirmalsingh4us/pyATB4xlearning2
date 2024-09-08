# method overridding - same name in the parent and child
# child always override the parent functions
# Super means  call my parent functions
class GrandFather:
    x = 20
    def home(self):
        print("Old home")

class Father(GrandFather):
    a = 10
    def home(self):
        print("3Bhk")
        print(super().x)
        print(super().home())

class Son(Father):
    def home(self):
        print(super().a) # We can also use father  Attribute by Super()
        super().home() # We can use Father behaivour by super()
        print("No Home")

Nirmal = Son()
Nirmal.home()
