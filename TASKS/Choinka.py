wysokosc = 5

for i in range(wysokosc):  # wiersze
    for j in range(wysokosc - i - 1):  # spacje
        print(' ', end='')
    for k in range(2 * i + 1):  # gwiazdki
        print('*', end='')
    print()  # nowa linia
    