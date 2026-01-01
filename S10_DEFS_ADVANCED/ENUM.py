import ZADANIE_PolaFigur
from enum import IntEnum
Menu_Figury = (IntEnum('Menu_Figury', {'Kwadrat':4, 'Prostokąt':52, 'Trójkąt':24, 'Trapez':3, 'Koło':7}))


#enumeration - spis - wyliczenie

print(ZADANIE_PolaFigur.rectangleArea(5, 5))

wybor = int(input("""Wybierz figurę, której pole chcesz obliczyć:
       1.Kwadrat
       2.Prostokąt
       3.Trójkąt
       4.Trapez
       5.Koło
    """))

if (wybor == Menu_Figury.Kwadrat):
    a = int(input("Podaj bok kwadratu: "))
    print(ZADANIE_PolaFigur.squareArea(a))
elif (wybor == Menu_Figury.Prostokąt):
    a = int(input("Podaj bok a prostokąta: "))
    b = int(input("Podaj bok b prostokąta: "))
    print(ZADANIE_PolaFigur.rectangleArea(a, b))
elif (wybor == Menu_Figury.Trójkąt):
    a = int(input("Podaj bok trojkata: "))
    h = int(input("Podaj wysokosc trojkata: "))
    print(ZADANIE_PolaFigur.triangleArea(a, h))
elif (wybor == Menu_Figury.Trapez):
    a = int(input("Podaj bok a trapezu: "))
    b = int(input("Podaj bok b trapezu: "))
    h = int(input("Podaj bok h trapezu: "))
    print(ZADANIE_PolaFigur.trapezArea(a, b, h))
elif (wybor == Menu_Figury.Koło):
    r = int(input("Podaj promieć koła: "))
    print(ZADANIE_PolaFigur.circleArea(r))
else: 
    exit