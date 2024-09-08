# static method
# it is a mthod that belongs to a class rather than instance of class
class Mathoperation:
    def div(self,a,b):
        return a/b

    @staticmethod  # static method can be called directely without object
    def Sum(a,b):
        return a+b

ob = Mathoperation()
output = ob.div(25,5)
print(output)

print(Mathoperation.Sum(66,33))