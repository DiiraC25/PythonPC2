def contar_digitos(numero, digito):
    cantidad = str(numero).count(str(digito))
    return cantidad
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese el dígito que desea contar: "))
cantidad_digitos = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad_digitos}")