# limitation with lambda function

def add_10(n):
    return n + 10

#o = add_10(100)
o = lambda n: n + 10
print(o(115))

def num1(a,b):
    return a+b
oo = lambda a,b : a + b
print(oo(a=5, b=15))