import os

archivo_alumnos = "alumnos.txt"

# Al iniciar: si no existe alumnos.txt, lo creamos vacío
if not os.path.exists(archivo_alumnos):
    open(archivo_alumnos, "w", encoding="utf-8").close()

# Leer alumnos y armar la lista + el diccionario
alumnos = []
diccionario_alumnos = {}

with open(archivo_alumnos, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            nombre, apellido, legajo, nota = linea.split(";")
            alumno = {"nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": float(nota)}
            alumnos.append(alumno)
            diccionario_alumnos[legajo] = alumno

# Menú principal
while True:
    print("\n===== GESTIÓN DE ALUMNOS =====")
    print("1. Ver alumnos")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        if not alumnos:
            print("\nNo hay alumnos registrados.")
        else:
            print("\n--- Lista de alumnos ---")
            for a in alumnos:
                print(f"{a['nombre']} {a['apellido']} - Legajo: {a['legajo']} - Nota: {a['nota']}")

    elif opcion == "2":
        # Nombre: solo letras
        while True:
            nombre = input("Nombre: ").strip()
            if nombre.replace(" ", "").isalpha():
                break
            print("Dato inválido: ingrese solo letras.")

        # Apellido: solo letras
        while True:
            apellido = input("Apellido: ").strip()
            if apellido.replace(" ", "").isalpha():
                break
            print("Dato inválido: ingrese solo letras.")

        # Legajo: 5 dígitos
        while True:
            legajo = input("Legajo (5 dígitos): ").strip()
            if legajo.isdigit() and len(legajo) == 5:
                break
            print("Legajo inválido: debe tener exactamente 5 dígitos.")

        # Validar que no exista
        if legajo in diccionario_alumnos:
            print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        else:
            # Nota: entre 1 y 10
            while True:
                texto_nota = input("Nota promedio (1 a 10): ").strip().replace(",", ".")
                try:
                    nota = float(texto_nota)
                    if 1 <= nota <= 10:
                        break
                    print("Nota inválida: debe estar entre 1 y 10.")
                except ValueError:
                    print("Nota inválida: debe ser un número.")

            # Guardar en el archivo
            with open(archivo_alumnos, "a", encoding="utf-8") as f:
                f.write(f"{nombre};{apellido};{legajo};{nota}\n")

            # Actualizar la lista y el diccionario en memoria
            alumno_nuevo = {"nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota}
            alumnos.append(alumno_nuevo)
            diccionario_alumnos[legajo] = alumno_nuevo

            print(f"Alumno {nombre} {apellido} (legajo {legajo}) guardado correctamente.")

    elif opcion == "3":
        aprobados = [a for a in alumnos if a["nota"] >= 6]
        with open("aprobados.txt", "w", encoding="utf-8") as f:
            for a in aprobados:
                f.write(f"{a['nombre']};{a['apellido']};{a['legajo']};{a['nota']}\n")

        print(f"\nSe generó el archivo aprobados.txt con {len(aprobados)} alumno(s) aprobado(s).")
        with open("aprobados.txt", "r", encoding="utf-8") as f:
            print(f.read())

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")

