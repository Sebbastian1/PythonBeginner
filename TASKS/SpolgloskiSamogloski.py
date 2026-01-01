tekst = "Programowanie w pythonie jest super"

samogloski = ['a', 'o', 'i', 'e', 'u', 'y']

spolg = []
samog = []

for litera in tekst:
    if litera.isalpha():   
        if litera in samogloski:
            samog.append(litera)
        else:
            spolg.append(litera)

xd = len(samog)
print(xd)
print ("Spolgloski:", spolg,"\n","Samogloski", samog)