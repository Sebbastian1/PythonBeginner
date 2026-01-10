#with - gdy otworzymy to mamy pewność że zostanie zamkniety, unikamy file.close()
with open("test.txt", "w") as file: #UCHWYT/HANDLE
    file.write("sample \n")
    file.write("xd")
    print(0/0)
    file.write("Co")

#finally wykonuje sie zawsze, nawet jak się coś zepsuje po
