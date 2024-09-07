class A:
    def method(self):
        return "Method A"

class B:
    def method(self):
        return "Method B"

class C(B,A):
    pass

cc = C()
print(cc.method())