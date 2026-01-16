fileName = input(str("Podaj nazwę pliku: "))

def ifContains(value):
    try:
        with open(value, "r", encoding="UTF-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")

ifContains(fileName)
