# Overloading
# Python does not support method overloading
# in the traditional sense

class Mathulis (object): # is - A object of  single inheritance
# method - overloading is not supported
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=30):
        return a+b+c

math = Mathulis()
op1 = math.add(5,3)
print(op1)
