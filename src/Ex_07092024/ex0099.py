class Grandparent:
    Key_gold ="1kg"
    def grandparent_method(self):
        return "Grandparent Method"

class Parent(Grandparent):
    def Parent_method(self):
        return "Parent Method"


class Child(Parent):
    mac_m3_apple = "M3 MAx"
    def child_method(self):
        return "Child Method"

child = Child()
print(child.grandparent_method())