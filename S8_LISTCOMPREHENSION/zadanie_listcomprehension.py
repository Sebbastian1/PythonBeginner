#Zbuduj listę kwadratów tylko dla liczb podzielnych przez 3
liczba = [(element, element**2) for element in range(51) if (element % 3 == 0)]
print (liczba)

#Zamień słowa na wielkie litery, ale tylko te dłuższe niż 3 litery

slowa = ["kot", "pies", "hipopotam", "dom", "samochód", "ok"]

duze = [slowo.upper() for slowo in slowa if len(slowo) > 3]

print(duze)