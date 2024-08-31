# understanding in decorator in python
# basiclly way to modify the bahaviour of a function
# it is powerful tool that allow you to wrap another function and extend its functionality
# while kepping the origial function code unchanged

# two part wrapper & call

def my_decorator(func):
    def wrapper():
        print("Something is happening befor the funcation is called")
        print("Add helmet", "gloves")
        func()
        print("something is happening after the funcation is called")
        print("Secure driving")

    return wrapper()

    #  @my_decorator
    # def drive_bike():
    #   print("I am driving bike")




@my_decorator
def drive():


    print("car driving")
