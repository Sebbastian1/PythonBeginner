'''
numbers = [3, 10, -5, 8, 0, -2, 7, 10, -5]

print (max(numbers), min(numbers))
print (sum(numbers))
numbersEven = [element for element in numbers if (element > 0)]
print(numbersEven)
numbersSquared = [element**2 for element in numbers]
print(numbersSquared)
numbersTen = numbers.count(10)
print(numbersTen)
'''
"""
numbers = [4, -3, 7, 0, -1, 8, 5, -6]

max_value = numbers[0]

for element in numbers:
    if element > max_value:
        max_value = element

print(max_value)

min_value = numbers[0]

for element in numbers:
    if element < min_value:
        min_value = element

print(min_value)

wynik = 0
for element in numbers:
    wynik = wynik + element
print(wynik)


print("Liczby ujemne:")
count_negative = 0
for element in numbers:
    if element < 0:
        count_negative += 1
print(count_negative)

abs_numbers = []
print("Wartości bezwzględne:")
for element in numbers:
    if element < 0:
        abs_numbers.append(-element)
    else:
        abs_numbers.append(element)
print(abs_numbers)
"""

numbers = [6, -2, 0, -9, 4, -1]

negative = 0
for element in numbers:
    if element < 0:
        negative += 1
print (negative)
    
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = -numbers[i]
print (numbers)