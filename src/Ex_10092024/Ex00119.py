# try ,except, finally
print("-----Start the program-----")
try:
    num1 = int(input("enter the num1\n"))  # ValueError: invalid literal for int() with base 10: 'p'
    num2 = int(input("enter the num2\n"))
    result = num1/ num2  # ZeroDivisionError: division by zero
    #print("Result Div is ", result)
except ValueError as ve: # exception is class
    print("Value Error, you enter string value instead of Int value")
except ZeroDivisionError as zde:
    print("Zero Division error, Plz don't user 0 in num2")
else:
    print(f"Result is {result}")
finally:
    print("This is final code for execution..!")

