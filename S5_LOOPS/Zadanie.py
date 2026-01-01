wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj liczbę parzystą: "))
    if x%2 == 0:
        wynik += x
    else:
        print("To jest liczba nieparzysta!")
        continue
    i += 1
print ("Wynik z dodawania to:", wynik)