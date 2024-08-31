def outer_function():
    var1 = 30  # local int variable
    # print(var1)

    def inner_Func():
          print(var1)
    def inner_Func2():
        print(var1)

    inner_Func()
    inner_Func2()


outer_function()
