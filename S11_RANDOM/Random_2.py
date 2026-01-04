"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości

"""

import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia", "losowa rzecz"]

nagrodaZeSkrzynki = ["zielona", "niebieska", "purpurowa", "legendarna"]

from collections import Counter
print(Counter(random.choices(nagrodaZeSkrzynki, [80,15,4,1] ,k = 100)))


