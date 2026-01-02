'''
Time module
'''
import time

#Petla - 1 sposob
def sumuj_do(liczba): 
    n = 0
    for liczba in range (1, liczba + 1):
        n = n + liczba
    return n

#List comprehension - 2 sposob
def sumuj_do2(liczba): 
    return sum([liczba for liczba in range (1, liczba + 1)])

#List comprehension - 2 sposob
def sumuj_do3(liczba): 
    return sum({liczba for liczba in range (1, liczba + 1)})

#List comprehension - 2 sposob
def sumuj_do4(liczba): 
    return sum((liczba for liczba in range (1, liczba + 1)))

#Suma dwoch skrajnych liczb przez iloraz razy ostatnia liczba - sposob
def sumuj_do5(liczba): 
    wynik = (1 + liczba) / 2 * liczba
    return wynik

#Funkcja licząca czas

def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

print(function_performance(sumuj_do, 500000))
print(function_performance(sumuj_do2, 500000))
print(function_performance(sumuj_do3, 500000))
print(function_performance(sumuj_do4, 500000))
print(function_performance(sumuj_do5, 500000))

