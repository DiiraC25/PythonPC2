def imprimir_patron(filas):
    for i in range(1, filas * 2):
        if i <= filas:
            print('* ' * i)
        else:
            print('* ' * (filas * 2 - i))
imprimir_patron(5)