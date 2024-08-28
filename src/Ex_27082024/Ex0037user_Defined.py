# user defined
# can't return-> non return
# they can return something
# They have parameter
# They don't parameter/arguments

def greet():
    print("Hello World")


result = greet()
print(result)


# 2.
def greet_by_name(name):
    print("hello,", name)


greet_by_name("Nirmal singh")

#3.  # no return type and with default argument


def greet_by_default_arg(name="Mehtab"):
    print("How are you,", name)

    greet_by_default_arg("Gurfateh")
    greet_by_default_arg(name)
