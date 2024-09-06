class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #    print("DC")

    def sum(self, a, b):
        return self.a + self.b

    def sub(self, a, b):
        return self.a - self.b

    def mul(self, a, b):
        return self.a * self.b

    def div(self, a, b):
        return self.a / self.b


obj_ref = Calc(3, 6)
op = obj_ref.sum()
print(op)
