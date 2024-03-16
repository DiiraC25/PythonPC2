def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'
    cadena_sin_vocales = ''
    for letra in cadena:
        if letra not in vocales:
            cadena_sin_vocales += letra
    return cadena_sin_vocales
texto = input("Ingrese una cadena de texto: ")
texto_sin_vocales = omitir_vocales(texto)
print("Texto con las vocales omitidas:", texto_sin_vocales)