def obtener_fecha_en_formato_ymd(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    
    partes = fecha.split()
    if "/" in fecha:
        partes = fecha.split("/")
        mes = partes[0]
        dia = partes[1]
        año = partes[2]
        if not año.isdigit():
            return "El año debe ser un número."
        año = "19" + año if int(año) <= 21 else "19" + año
    else:
        mes = partes[0]
        dia = partes[1][:-1]
        año = partes[2]

    mes = meses[mes] if mes in meses else mes
    dia = f"{dia:02}"
    año = f"{año:04}"

    return f"{año}-{mes}-{dia}"

fecha_input = input("Ingrese una fecha (en formato mes/día/año o mes día, año): ")
fecha_ymd = obtener_fecha_en_formato_ymd(fecha_input)
print("La fecha en formato AAAA-MM-DD es:", fecha_ymd)