names = {"Arkadiusz", "wioletta", "karol", "Sebastian", "Jakub", "Agniecha"}

names = {name for name in names if not name.startswith("A")}

print (names)