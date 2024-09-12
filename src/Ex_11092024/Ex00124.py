# custom Exception -> user defined exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 1000
withdraw = int(input("Enter the amount you want to withdraw!!\n"))
if withdraw > balance:
    raise MyCustomException("Balance is low !")
else:
    print("Remain Balance :",(balance-withdraw))

