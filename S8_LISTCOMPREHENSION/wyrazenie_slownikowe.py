names = {"Arkadiusz", "Wioletta", "Karol", "Sebastian", "Jakub", "Agniecha"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

namesLength = {name : len(name) for name in names if name.startswith("A")}

print(namesLength)

multiplied = {number : number**3 for number in numbers}

print(multiplied)

#Zamien stopnie celcjusza na fahrenheit

fahrenheit = {key : (celcius)*(9/5)+32 for key, celcius in celcius.items() if(celcius>-5) if (celcius<20)}

print (fahrenheit)