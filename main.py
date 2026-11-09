print("SISTEMA DE REGISTRO DE ESTUDIANTES")
print("1. Registrar estudiante")
print("2. Consultar estudiantes")
print("3. Salir")

estudiantes = []

def registrar_estudiante(nombre):
    estudiantes.append(nombre)
    print("Estudiante registrado:", nombre)

registrar_estudiante("Juan Pérez")
registrar_estudiante("María López")

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

def consultar_estudiantes():
    print("ESTUDIANTES REGISTRADOS")
    for estudiante in estudiantes:
        print(estudiante)

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

# Ejemplo de uso opcional
notas = [85, 90, 78, 92]
print("Promedio de calificaciones:", calcular_promedio(notas))