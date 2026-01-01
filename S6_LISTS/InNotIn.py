imiona = ["skusa", "misha", "dupisha", "grisha", "kisha"]
liczby = [1,5,15,18,23]

if ("skusa" in imiona):
    print("Hi skuska")

if (2 not in liczby):
    print("nie ma liczby 2")
else:
    print("Liczba 2 znajduje sie w liscie")

print ([4,20,15] + liczby) #dodawanie przed listą 

nowe_liczby = ([4,20,15] + liczby)

print ("Nowe: ",nowe_liczby)