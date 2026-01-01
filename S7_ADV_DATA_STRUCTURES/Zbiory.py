"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy          NIE           TAK             TAK                   TAK
krotki         NIE           TAK             NIE                   NIE
słowniki       TAK           NIE             TAK                   TAK
zbiory         TAK           NIE             NIE                   TAK

        ZBIORY: BONUS w postaci | & - ^ 
"""
#Wartości losowo ustawione

A = {1, 4, 20, -4, 20}
B = {2, 4, 15, 20, 7}

A.add(7)
#Usuwa 24 ze zbioru gdy występuje - gdy go nie ma, w przeciwienstwie do .remove, nie zwraca błędu gdy 24 nie ma w secie 
A.discard(24)

#Wyciąganie wartości wspólnych ze zbioru
print(A&B)

#Sprawdzenie elementów wszystkich ze zbiorów w tym samym momencie
print(A|B)

#Sprawdzenie elementów występujących w B a nie występujących w A
print(B-A)

#Elementy które są w A lub B, ale nie w obu na raz
print(A^B)

#Sprawdzenie czy zbiór A jest podzbiorem zbioru B - sprawdzamy czy każdy element A znajduje się w B
print (A.issubset(B))
# zanmiana listy w zbiór:
# print(set(A)) - gdyby A było listą 