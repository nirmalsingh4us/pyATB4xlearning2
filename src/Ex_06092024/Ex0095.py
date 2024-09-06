class Parent :
    gold = "2kg"

    def bhk2(self):
        print("2bhk")

class Child(Parent):
    diamond = "Diamond"
    def bhk3(self):
        print("3Bhk")

child_obj = Child()
print(child_obj.gold)
print(child_obj.diamond)
child_obj.bhk2()
child_obj.bhk3()

par_obj = Parent()
print(par_obj.gold)
par_obj.bhk2()