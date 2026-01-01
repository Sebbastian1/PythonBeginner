print("Program do dodawania słów, wciśnij odpowiednią cyfrę aby dodać słowo", "\n")

print("1. Dodaj słowo")
print("2. Szukaj słowa")
print("3. Usuń słowo")
print("4. Wyświetl listę")
print("5. Zakończ działanie programu")

listaSlow = []

while True:
    opcja = int(input("Wybierz opcję:"))
    if opcja == 1:
        dodaj = input("Słowo jakie chcesz dodać:")
        listaSlow.append(dodaj)
    elif opcja == 2:
        szukaj = input("Słowo, którego chcesz wyszukać:")
        if szukaj in listaSlow:
            print("Jest takie słowo w liście!")
        else:
            print("Nie ma takiego słowa")  
    elif opcja == 3:
        usun = input("Podaj słowo które chcesz usunąć:")   
        if usun in listaSlow:
            listaSlow.remove(usun)
            print("Usunięto słowo", usun, "z listy")
        else:
            print("Nie ma takiego słowa w liście")
    elif opcja == 4:
        print("Oto lista słów:")
        print(listaSlow)

    elif opcja == 5:
        print("Koniec programu")
        break 
    else:
        print("Podaj poprawną cyfrę!")

    print("1. Dodaj słowo")
    print("2. Szukaj słowa")
    print("3. Usuń słowo")
    print("4. Wyświetl listę")
    print("5. Zakończ działanie programu")