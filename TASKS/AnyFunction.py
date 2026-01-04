#Use any() function to check that list has even numbers

numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]

def any_even(wartosc):
    numbers1 = any([liczba % 2 == 0 for liczba in wartosc])
    return numbers1

# any - jakikolwiek - sprawdza czy jakakolwiek wartość to True
# all - wszystkie

print (any_even(numbers1))
print (any_even(numbers2))