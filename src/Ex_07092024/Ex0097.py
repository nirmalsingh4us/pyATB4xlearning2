# Multiple Inheritence
class Father:
    key = "abc"
    __password = "Password"

    def __Show_password(self):
        print(self.__password)

    def father_money(self):
        return 5

    def home(self):
        return "This is from the Father"

    def show_everything(self):
        print(self.__password)

class Mother:
    def mother_money(self):
        return 2
    def home(self):
        return "This is from the Mother"

class Son(Father,Mother): # Method resolution order
    pass

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home()) # there is Diamond problem,
s.show_everything()
