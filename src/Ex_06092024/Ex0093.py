class Bank:

    def __init__(self,account_no, balance):
        self.balance = balance
        self.__accountno = account_no

    def deposit(self,amount):
        self.balance = self.balance + amount

    def chk_balance(self):
        print(self.balance)

    def show_me_account_no(self, is_auth):
        if is_auth == True:
            print(self.__accountno)
        else:
            print("You are not allowed !")

axis = Bank(9780527515,200)
axis.deposit(100)
axis.chk_balance()
axis.show_me_account_no(False)
axis.deposit(500)
axis.chk_balance()
