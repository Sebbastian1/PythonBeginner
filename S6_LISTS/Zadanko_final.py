#Znajdź liczby od 100 do 470 włącznie, które są:
# podzielne przez 7 i są niepodzielne przez 5

wynik = [liczba for liczba in range(2, 471) if liczba % 7 == 0 and liczba % 5 != 0]

print(wynik)