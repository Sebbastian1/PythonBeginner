#Zsumuj wszystkie liczby od zera do 100, podniesione do potęgi 2

generator = (element**2 for element in range(101))
print(sum(generator))

