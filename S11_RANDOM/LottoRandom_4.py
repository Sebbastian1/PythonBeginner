import random
"""
def losujLiczbe(how_many, total):
    list = []
    while len(list) < how_many:
        i = random.randrange(0, total)
        if i not in list:
            list.append(i)
    return list

print(losujLiczbe(6, 49))
"""
# sample
"""
def choose_random_numbers(amount, total):
    print(random.sample(range(total+1), amount))

choose_random_numbers(6, 49)
"""
cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

random.shuffle(cardList)

player_1 = []
player_2 = []
for i in range (5):
    karta = cardList.pop()
    player_1.append(karta)
    karta = cardList.pop()
    player_2.append(karta)

print (player_1, player_2)
