# Web Automation - selenium
# page - you are going to automate

class VWOloginpage :
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "NS_TEST@gmail.com" and self.password == "abc123":
            print("Allowed to login!")
        else:
            print("Not Allowed !")


email = input("Enter your Emailid \n")
password = input("Enter your password \n")

vwo_obj = VWOloginpage(email, password)
vwo_obj.login_confirm()
print(vwo_obj)
