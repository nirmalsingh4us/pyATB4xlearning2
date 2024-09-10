print("-----Start the program-----")
try:
    a = int(input("enter the num1\n"))  # ValueError: invalid literal for int() with base 10: 'p'
    b = int(input("enter the num2\n"))
    c = a / b  # ZeroDivisionError: division by zero
    print("Result Div is ", c)
except Exception as e: # exception is class
    print(e)
    print("Please check your inputs, it shouldn't be a string or zero")
    print("-----end the program-----")
