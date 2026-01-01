print("Program do zarządzania definicjami słów\n")

def pokaz_menu():
    print("\n1. Dodaj definicję")
    print("2. Szukaj definicji")
    print("3. Usuń definicję")
    print("4. Wyświetl wszystkie definicje")
    print("5. Zakończ działanie programu\n")

listaSlow = {}

pokaz_menu()

while True:
    try:
        opcja = int(input("Wybierz opcję (1-5): "))
    except ValueError:
        print("❌ Wprowadź liczbę od 1 do 5.")
        continue

    if opcja == 1:
        klucz = input("Podaj słowo do zdefiniowania: ").strip()
        definicja = input("Podaj definicję dla powyższego słowa: ").strip()
        listaSlow[klucz] = definicja
        print("✅ Pomyślnie dodano definicję!")

    elif opcja == 2:
        szukaj = input("Słowo, którego chcesz wyszukać: ").strip()
        if szukaj in listaSlow:
            print(f"🔎 Definicja dla '{szukaj}': {listaSlow[szukaj]}")
        else:
            print("❌ Nie znaleziono takiego słowa w słowniku.")

    elif opcja == 3:
        usun = input("Podaj słowo, które chcesz usunąć: ").strip()
        if usun in listaSlow:
            del listaSlow[usun]
            print(f"🗑️ Usunięto słowo '{usun}' z listy.")
        else:
            print("❌ Nie ma takiego słowa w słowniku.")

    elif opcja == 4:
        if listaSlow:
            print("📚 Lista definicji:")
            for slowo, definicja in listaSlow.items():
                print(f"- {slowo}: {definicja}")
        else:
            print("⚠️ Słownik jest pusty.")

    elif opcja == 5:
        print("👋 Kończę działanie programu.")
        break

    else:
        print("❌ Nieprawidłowa opcja. Wybierz od 1 do 5.")

    pokaz_menu()