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

def finish_timer(start):
    end = time.perf_counter()
    return end - start

start = time.perf_counter()
print(sumuj_do(500))
print(finish_timer(start))
start = time.perf_counter()
print(sumuj_do2(500))
print(finish_timer(start))
start = time.perf_counter()
print(sumuj_do3(500))
print(finish_timer(start))
start = time.perf_counter()
print(sumuj_do4(500))
print(finish_timer(start))
start = time.perf_counter()
print(sumuj_do5(500))
print(finish_timer(start))


