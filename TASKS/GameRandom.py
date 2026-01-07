"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
niebieski - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""

import random
from enum import Enum

whichLevel = 0

Event = Enum('Event', ['Chest', 'Empty'])
Colour = Enum('Colour' ['green': 'zielony', 'blue': 'niebieski', 'purple': 'fioletowy', 'gold': 'złoty'])

chestEvent = {
                Event.Chest: 0.6,
                Event.Empty: 0.4
             }

colourEvent = {
                Colour.green: 0.75,
                Colour.blue: 0.2,
                Colour.purple: 0.04,
                Colour.gold: 0.01
              }


eventList = tuple(chestEvent.keys())
eventProbability = tuple(chestEvent.values())

colourList = tuple(colourEvent.keys())
colourProbability = tuple(colourEvent.values())

print("Witamy w grze!")

while (whichLevel < 5):
    playerChoice = input("Do you want to go forward (type: yes)?: ")
    if playerChoice == 'yes':
        print("Let's move forward!")
        isInChest = random.choice(eventList)
        if isInChest == Event.Chest:
            print("Congratulations, the chest contains something!")
            chestColour = random.choice(colourList, colourProbability)[0]
             
        else:
            print("The chest is empty! Maybe in the next room!")
    else:
        print("This answer is not right, you can only type: 'yes' xd")
        continue
    
    print("That's it, thank you for the game")
    whichLevel = whichLevel + 1