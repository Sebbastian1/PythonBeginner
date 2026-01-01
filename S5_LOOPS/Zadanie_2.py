szukanaLiczba = 12
y = 0
while y != szukanaLiczba:
    y = int(input("Podaj liczbę z zakresu od 0 do 20: "))
    if y < szukanaLiczba:
        print("Podana liczba jest za mała!")
        continue
    elif y == szukanaLiczba:
        print("To ta liczba!")
        break
    else:
        print("Podana liczba jest za duża!")
        continue




