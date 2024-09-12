class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number \n"))
        except Exception as E:
            print("Enter the int value of a")
        else:
            print(a)
        finally:
            print("Finally : anyhow i will be printed")

x = XYZ()
x.f1()