#r+ - do czytania i pisania
#w+ - do czytania i pisania, usuwa poprzednią zawartość pliku
#a+ - wieczny tryb dopisywania i czaytania

with open("oceany.txt", "a+", encoding="UTF-8") as file:
    file.write("\nWielki oszyn")
    file.seek(0)
    file.readline()
    print(file.tell())