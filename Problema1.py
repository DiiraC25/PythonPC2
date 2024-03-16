def encontrar_numeros_divisibles():
    numeros_divisibles = []
    for numero in range(1500, 2701):
        if numero % 7 == 0 and numero % 5 == 0:
            numeros_divisibles.append(numero)
    return numeros_divisibles

resultado = encontrar_numeros_divisibles()
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 y 2700 son:")
print(resultado)