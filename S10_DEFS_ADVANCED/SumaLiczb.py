"""
Napisz program, który policzy sumę wszystkich liczb od 1 do podanej liczby 

Dla np.5 
1+2+3+4+5
zwróci 
15
"""

#Tradycyjnie
"""
# liczba = int(input("Podaj liczbę do której chcesz zwrócić sumę od 1: "))

# wynik = 0

# for i in range (1, liczba+1):
#     wynik += i

# print(wynik)
"""


#Funkcja1
"""
def sumujLiczby(liczba):
    wynik = 0
    for i in range (1, liczba+1):
        wynik += i
    return wynik


print(sumujLiczby(14))
"""

