numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Respuesta inválida. Por favor, responda SI o NO.")
numeros_pares = 0
numeros_impares = 0
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
print("Números ingresados:", numeros)
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)