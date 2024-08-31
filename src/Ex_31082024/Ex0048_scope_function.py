# scope of function
global_b = 25
def my_func():
    a =10
    print(a)
    print(global_b)
my_func()

def new_fun():
    print(global_b)


new_fun()