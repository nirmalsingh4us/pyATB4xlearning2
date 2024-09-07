class GF:
    def car(self):
        return "Old car"
class F(GF):
    def car(self):
        return "Honda Civic"
class S(F):
    def car(self):
        return "Lambo"

s = S()
gf = GF()
print(gf.car())
print(s.car())
