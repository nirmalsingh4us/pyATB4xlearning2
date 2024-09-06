class Calc:
   # def __init__(self):
    #    print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj_ref = Calc()
a = int(input("Enter the value a\n"))
b = int(input("Enter the value b\n"))
output_sum = obj_ref.sum(a, b)
output_sub = obj_ref.sub(a,b)
output_mul = obj_ref.mul(a,b)
output_div = obj_ref.div(a,b)
print(output_sum,output_sub,output_mul,output_div)
