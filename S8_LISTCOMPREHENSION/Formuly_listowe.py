liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []

#for element in liczby:
#    potegiDwojki.append(element**2)


liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

#odpowiednik 1 pętli - wyrażenie listowe, bez append
potegiDwojki2 = [element**2 for element in liczby]
print (potegiDwojki2)

#odpowiednik 2 pętli - bez metody append
liczbyParzyste = [element for element in liczby if (element % 2) == 0]

print(liczbyParzyste)

# [co zrobic na elementcie | for element in stara_lista | warunek oparty na elemencie]