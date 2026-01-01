import math
print("Witaj w programie do liczenia pól figur!")
print("Wybierz opcję 1-6:")
print("1.Pole prostokąta")
print("2.Pole kwadratu")
print("3.Pole trójkąta")
print("4.Pole trapezu")
print("5.Pole koła")

def rectangleArea(a, b):
    return a * b

def squareArea(a):
    return a * a

def triangleArea(a, h):
    return (a*h)/2

def trapezArea(a, b, h):
    return ((a+b)*h)/2

def circleArea (r):
    return math.pi*pow(r, 2)

opcja = int(input("Podaj opcję: "))

if opcja == 1:
    a = 5
    b = 3
    print (rectangleArea(a, b))
elif opcja == 2:
    a = 3
    print (squareArea(a))
elif opcja == 3:
    a = 5
    h = 6
    print (triangleArea(a, h))
elif opcja == 4:
    a = 5
    b = 3
    h = 5
    print (trapezArea(a, b, h))
elif opcja == 5:
    r = 3
    print (circleArea(r))
else:
    exit