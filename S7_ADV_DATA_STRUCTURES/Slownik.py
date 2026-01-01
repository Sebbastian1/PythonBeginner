#Tworzenie slownika KLUCZ - WARTOSC
pokoje = {'imie': 'Sebastian Boryś', 69: 'Weronika Broda'}


print (pokoje['imie'],"and", pokoje[69])

print (pokoje.get(69))

pokoje.update({69: 'siemaweras'})

print(pokoje)

pokoje.pop('imie')

print(pokoje)