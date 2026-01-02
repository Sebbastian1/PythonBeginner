'''
Napisz funkcję wykonaj_operacje(a, b, operacja), która:

przyjmuje dwie liczby a i b

przyjmuje funkcję operacja

zwraca wynik działania funkcji operacja(a, b)

Następnie:

Zdefiniuj funkcję dodaj(x, y), która zwraca sumę

Zdefiniuj funkcję pomnoz(x, y), która zwraca iloczyn

Wywołaj wykonaj_operacje:

raz z dodawaniem

raz z mnożeniem

'''

#zad1
'''
def dodaj(x, y):
    return x + y

def pomnoz(x, y):
    return x * y

def wykonaj_operacje(a, b, operacja):
    return operacja(a,b)

print(wykonaj_operacje(3, 4, dodaj))
print(wykonaj_operacje(3, 4, pomnoz))
'''
'''
#zad2

def odejmij(x, y):
    return x-y

def podziel(x,y):
    return x/y

def przetworz_liczby(a, b, operacja):
    return operacja(a, b)

print(przetworz_liczby(10, 5, odejmij))
print(przetworz_liczby(10, 5, podziel))
'''


def podwojn(n):
    return 2 * n

def zwieksz_o_jeden(n):
    return n + 1

def przetworz_liste(lista, operacja):
    nowa_lista = []
    for element in lista:
        nowa_lista.append(operacja(element))
    return nowa_lista

liczby = [1, 2, 3, 4]

print(przetworz_liste(liczby, podwojn))         
print(przetworz_liste(liczby, zwieksz_o_jeden)) 