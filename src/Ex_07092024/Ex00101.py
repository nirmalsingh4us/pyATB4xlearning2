# Hybrid Inheritance

# it is combination of multiple ,single,multilevel  inheritance

class A:
    def methodA(self):
        return  "Method A"
class B(A):
    def methodB(self):
        return "Method B"
class C(A):
    def Methodc(self):
        return "Method C"

class D(B,C):
    def Method_D(self):
        return "Method D"

d = D()
print(d.Method_D())
print(d.methodA())
print(d.methodB())
print(d.Methodc())
