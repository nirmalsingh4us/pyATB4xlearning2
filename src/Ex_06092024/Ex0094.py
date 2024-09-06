# Inheritance
# type of inheritance -> single,(80%),  Multiple, Multi-level, hybrid, hierarchical inheritance

class Father :
    key = "2bhk"

    def car(self):
        print("Father Car!!","Alto",self.key)


class Son(Father):
    pass

fatherobj = Father()
fatherobj.car()


son_obj = Son()
son_obj.car()