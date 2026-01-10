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

def randomizeValue(value):
    lowestValue = value - value * 0.1
    highestValue = value + value * 0.1
    return random.randint(int(lowestValue), int(highestValue))


whichLevel = 0
totalReward = 0

Event = Enum('Event', ['Chest', 'Empty'])
Colour = Enum('Colour', {'green': 'zielony', 'blue': 'niebieski', 'purple': 'fioletowy', 'gold': 'złoty'})

chestEvent = {
                Event.Chest: 0.8,
                Event.Empty: 0.2
             }

colourEvent = {
                Colour.green: 0.75,
                Colour.blue: 0.2,
                Colour.purple: 0.04,
                Colour.gold: 0.01
              }

rewardEvent = {
                Colour.green: 1000,
                Colour.blue: 4000,
                Colour.purple: 9000,
                Colour.gold: 16000
              }



eventList = tuple(chestEvent.keys())
eventProbability = tuple(chestEvent.values())

colourList = tuple(colourEvent.keys())
colourProbability = tuple(colourEvent.values())


print("Welcome in the game!")

while (whichLevel < 5):
    playerChoice = input("Do you want to go forward (type: yes)?: ")
    if playerChoice == 'yes':
        print("Let's move forward!")
        isInChest = random.choices(eventList, eventProbability)[0]
        if isInChest == Event.Chest:
            print("Congratulations, the chest contains something!")
            chestColour = random.choices(colourList, colourProbability)[0]
            print("You have found", chestColour.value, "chest!")
            reward = rewardEvent[chestColour]
            randomizedReward = randomizeValue(reward)
            print("Reward is:", randomizedReward)
            totalReward+=randomizedReward
        else:
            print("The chest is empty! Maybe in the next room!")
    else:
        print("This answer is not right, you can only type: 'yes' xd")
        continue
    
    whichLevel = whichLevel + 1

print("Ostatecznie udało ci się zebrać", totalReward, "złota")

