def liczbyDodatnie(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

numbers = [-5, 2, 0 ,3, -3, 96]

print (liczbyDodatnie(numbers))