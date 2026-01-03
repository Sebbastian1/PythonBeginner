# Argumenty kluczowe i pozycyjne
# W postaci :  klucz - wartość (domyślny)
# Pozycyjne - wtakie, których kolejność liczy się przy wywołaniu
 
def greet(name, message = "es", separator = " "):
    print(message, name, sep = separator)

greet("Seba","Siemano", "\n") 

# sep separuje pojedyncze słowa