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

listaGosciFinal1 = listaGosci|listaGosci2
listaGosciFinal2 = listaGosci&listaGosci2

print (listaGosciFinal1)
print (listaGosciFinal2)

#nie mozna miec listy w zbiorze