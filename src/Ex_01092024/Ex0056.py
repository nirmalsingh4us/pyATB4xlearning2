# other type of decorator
# static method, class, property, functool.wraps these will use in oops
# Decorator is used to store log value.
def dec1(func):
    def wrapper():
        print("dec 1")

    func()

    return wrapper


def dec2(func):
    def wrapper():
        print("dec 2")

    func()


    return wrapper


@dec2
@dec1
def say_hello():
    print("Hello Nirmal singh")
say_hello()