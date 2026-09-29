# ==========================================
# GESTIÓN DE NOTAS DE ESTUDIANTES - UTN
# ==========================================

# 1. Diccionario de alumnos (Legajo: Apellido y Nombre)
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 2. Lista de materias de 2 dimensiones[cite: 2]
# Estructura inicial: [Materia, Nota 1, Nota 2, Nota Final]
# Dejamos las notas vacías o en 0 para cargarlas luego.
materias = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0]
]

# 3. Lista de notas finales por alumno[cite: 2]
# Estructura: [Nombre del alumno, Promedio General]
notas_finales = [
    ["Rodolfo Fernandez", 0],
    ["Luis Gomez", 0],
    ["Andrea Pereira", 0],
    ["Juan Cruz Gonzales", 0]
]

# Variables para estadisticas generales
mejor_alumno = ""
mejor_promedio_general = 0

# Índice para recorrer la lista notas_finales en paralelo con el diccionario
indice_alumno = 0

# Iterar el diccionario de alumnos[cite: 2]
for legajo, nombre in alumnos.items():
    print(f"\n----------------------------------------")
    print(f"Alumno: {nombre} (Legajo: {legajo})")
    print(f"----------------------------------------")
    
    suma_notas_finales_materias = 0
    
    # Recorrer la lista de materias para cada alumno[cite: 2]
    for i in range(len(materias)):
        nombre_materia = materias[i][0]
        print(f"Ingrese las notas para la materia {nombre_materia}")
        
        # Validar Nota 1 (entre 0 y 10)[cite: 2]
        nota1 = int(input("Nota 1: "))
        while nota1 < 0 or nota1 > 10:
            print("Error. La nota debe estar entre 0 y 10.")
            nota1 = int(input("Nota 1: "))
            
        # Validar Nota 2 (entre 0 y 10)[cite: 2]
        nota2 = int(input("Nota 2: "))
        while nota2 < 0 or nota2 > 10:
            print("Error. La nota debe estar entre 0 y 10.")
            nota2 = int(input("Nota 2: "))
            
        # Calcular la Nota Final de la materia (promedio de las 2 notas)[cite: 2]
        nota_final_materia = (nota1 + nota2) / 2
        print(f"Nota Final {nombre_materia}: {nota_final_materia}")
        
        # Guardar en la estructura de materias (pisando los valores o actualizándolos)
        materias[i][1] = nota1
        materias[i][2] = nota2
        materias[i][3] = nota_final_materia
        
        suma_notas_finales_materias += nota_final_materia

    # Calcular el promedio general del alumno (promedio de las notas finales de las materias)[cite: 2]
    promedio_general = suma_notas_finales_materias / len(materias)
    
    # Guardar en la lista notas_finales
    notas_finales[indice_alumno][1] = promedio_general
    indice_alumno += 1
    
    # Determinar si es el mejor promedio general hasta el momento
    if promedio_general > mejor_promedio_general:
        mejor_promedio_general = promedio_general
        mejor_alumno = nombre

# Mostrar por pantalla la lista de materias completa del último alumno procesado[cite: 2]
print("\n========================================")
print("ESTADO FINAL DE MATERIAS (Último alumno)")
print("========================================")
for m in materias:
    print(f"Materia: {m[0]} | Nota 1: {m[1]} | Nota 2: {m[2]} | Nota Final: {m[3]}")

# Mostrar el mejor alumno de todos[cite: 2]
print("\n========================================")
print(f"RESULTADO GENERAL")
print(f"El mejor alumno es {mejor_alumno} con un promedio general de {mejor_promedio_general}")
print("========================================")