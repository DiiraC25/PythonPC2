def ingresar_alumnos():
    alumnos = []
    n = int(input("Ingrese el número de alumnos: "))
    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        calificaciones = []
        for j in range(3):
            calificacion = float(input(f"Ingrese la calificación {j+1} del alumno {nombre}: "))
            calificaciones.append(calificacion)
        alumno = {"Alumno": nombre, "Notas": calificaciones}
        alumnos.append(alumno)
    return alumnos
def mostrar_listado(alumnos):
    print("\nListado de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Calificaciones: {alumno['Notas']}")
alumnos = ingresar_alumnos()
mostrar_listado(alumnos)