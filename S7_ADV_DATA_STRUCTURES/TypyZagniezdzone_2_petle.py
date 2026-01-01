#Typy zagnieżdżone

imie = "Sebastian"
wiek = 24
plec = "mezczyzna"

imie2 = "Weronika"
wiek = 22
plec = "kobieta"

osoba1 = ('Sebastian', 24, 'mezczyzna')
osoba2 = ('Weronika', 22, 'kobieta')
osoba3 = ('Maniek', 25, 'mezczyzna')

#Lista w liście
listaGosci = {
    ('Sebastian', 24, 'mezczyzna'),
    ('Weronika', 22, 'kobieta'),
    ('Maniek', 25, 'mezczyzna')
}

listaGosci2 = {
    ('Sebastian', 24, 'mezczyzna'),
    ('W', 22, 'kobieta'),
    ('M', 25, 'mezczyzna')
}

listGosci3 = listaGosci & listaGosci2


for imie, wiek, plec in listaGosci:
    print ("Imię:",imie)
    print ("Wiek:",wiek)
    print ("Płeć:",plec)
    print("\n")