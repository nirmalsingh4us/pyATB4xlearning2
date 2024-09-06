# Multi level heritance

class Grandfather:
    gold = "2kg"

    def bhk1(self):
        print("Bhk1")


class Father(Grandfather):
    diamond = "22 karat"

    def bhk2(self):
        print("2Bhk")


class Son(Father):
    btc = "1 BTC"


    def bhk3(self):
        print("3Bhk")


s = Son()
s.bhk1()
s.bhk2()
s.bhk3()
f = Father()
f.bhk2()
f.bhk1()
gf = Grandfather()
gf.bhk1()
