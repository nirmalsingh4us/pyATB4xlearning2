# Hybrid Inheritance
class Father :
    def House(self):
        print("300 Sq feet")

class Nirmal(Father):
    def Nirmal_house(self):
        print ("100 sq.feet")

class Avtar(Father):
    def avtar_house(self):
        print("200 Sq.feet")

class Jatinder(Father):
    def Jatinder_house(self):
        print("No house in Janta Colony")

Nir = Nirmal()
Nir.House()
Nir.Nirmal_house()

print("%^%^%^%^%^%^%^%^")

Avt = Avtar()
Avt.avtar_house()
Avt.House()
print("%^%^%^%^%^%^%^%^")
Jet= Jatinder()
Jet.House()
Jet.Jatinder_house()