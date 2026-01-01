#len() - długość
#.append - dodać
#.extend - rozszerzyć
#.insert(index, co)- wstawić
#.index - indeks danego elementu
#sort(reverse=False) - sortuj rosnąco
#max()
#min()
#.count - ile razy coś wystąpi
#.pop - usuń ostatni element
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyść listę
#.reverse - zamień kolejność

lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]

print(len(lista1)) # 5 elementów

#lista1.append(4) # dodaje 4 na końcu lista1
print(lista1)

#lista1.append([2,4,5]) #dodaje liste w liste
print(lista1)

lista1.extend([2,4,5]) #dodaje do aktualnej listy
print(lista1)

#lista1.insert(1, "Misha") #wstaw do listy (numer, treść)
#print(lista1)

print(lista1.index(5)) #wypisuje indeks liczby wpisanej

lista1.sort(reverse=True) #sortuje od najmniejszej do największej 

print(lista1)

print(min(lista1)) #minimalna wartość dla listy

print(lista1.count(1)) #liczy ile razy wystąpiła cyfra 1

lista1.pop()
print(lista1)

lista1.remove(1) #usuwa pierwszą 1 

print(lista1)

#lista1.clear() #czyscimy liste
#print(lista1)

lista1.reverse()
print(lista1)