#Obiekt - zmienna w której można wywołać też
#funkcje i może mieć więcej niż 1 wartość
# Obiekty immutable (niezmienne): bool, int, float, tuple, str
 

a = 257

listSample = [1, 4 , 512, 24]

listSample2 = listSample #Przypisanie adrestu (mutable)


c = 5
print (id(c))
def add (c, amount = 1):
    print (id(c))
    c = c + amount
    print (id(c))

add(c)

def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSample))
append_element_to_list(listSample, 5)