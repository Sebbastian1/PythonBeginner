import sys

#Zajmuje od razu miejsce w pamięci 
evenNumbers = [element for element in range(4400) if(element%2==0)]

#Zajmuje miejsce w pamięci np dopiero przy przejściu w pętli - oszczędza pamięć
evenNumbersGenerator = (element for element in range(400) if (element % 2 == 0))

print (evenNumbersGenerator)

print(sys.getsizeof(evenNumbers))

for item in evenNumbersGenerator:
    print(item)