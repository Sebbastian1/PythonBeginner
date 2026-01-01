import ZADANIE_PolaFigur

print(ZADANIE_PolaFigur.rectangleArea(5, 5))

wybor = input ("""Wybierz figurę, której pole chcesz obliczyć:
       1.Kwadrat
       2.Prostokąt
       3.Trójkąt
       4.Trapez
       5.Koło
        """)

if (wybor == '1'):
    a = int(input("Podaj bok kwadratu: "))
    print(ZADANIE_PolaFigur.squareArea(a))
elif (wybor == '2'):
    a = int(input("Podaj bok a prostokąta: "))
    b = int(input("Podaj bok b prostokąta: "))
    print(ZADANIE_PolaFigur.rectangleArea(a, b))
elif (wybor == '3'):
    a = int(input("Podaj bok trojkata: "))
    h = int(input("Podaj wysokosc trojkata: "))
    print(ZADANIE_PolaFigur.triangleArea(a, h))
elif (wybor == '4'):
    a = int(input("Podaj bok a trapezu: "))
    b = int(input("Podaj bok b trapezu: "))
    h = int(input("Podaj bok h trapezu: "))
    print(ZADANIE_PolaFigur.trapezArea(a, b, h))
elif (wybor == '5'):
    r = int(input("Podaj promieć koła: "))
    print(ZADANIE_PolaFigur.circleArea(r))
else: 
    exit