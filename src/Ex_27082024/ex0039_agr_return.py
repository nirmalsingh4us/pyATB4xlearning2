# 3.  # no return type and with default argument


def greet_by_default_arg(name="Mehtab"):
    print("How are you,", name.upper())


greet_by_default_arg("Gurfateh")
greet_by_default_arg()
greet_by_default_arg(name="Paramjit")  # positional arguments


def multiple_arg(name1="Avtar", name2="jatinder", name3="sonia"):
    print("multiple Arguments", name1, name2, name3)


multiple_arg(name1="manu", name2="dishu", name3="agam")
