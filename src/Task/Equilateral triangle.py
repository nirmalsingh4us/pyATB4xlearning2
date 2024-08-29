# Triangle Classifier
# Equilateral, Isosceles and scalene

a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))
c = float(input("Enter the side c: "))

if a == b == c:
    print("This is Equilateral Trianlge")
elif a == b or b == c or c == a:
    print("This is isosceles Triangle")
else:
    print("This is scalane")
