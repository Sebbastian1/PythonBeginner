imiona = ['Arkadiusz', 'Wiola', 'Antek']

imie = input("Podaj imię by sprawdzić czy masz dostęp: ")
imie = imie.capitalize()
if imie in imiona:
    print("Masz dostęp")
else:
    print("Brak dostępu")