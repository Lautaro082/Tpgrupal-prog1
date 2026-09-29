#---------------------PRÁCTICA INTEGRADORA 1 - PYHTON-------------------------------------------

#PRACTICA A - MÁQUINA EXPENDEDORA 

#Lista de 2 dimensiones: código, golosina, stock

golosinas = [
    [1, "Alfajor Fulbito", 20],
    [2, "Chicles", 50],
    [3, "Gomitas Mogul", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Tita", 10],
    [7, "Jugo Baggio", 10],
    [8, "Papas Lays", 2],
    [9, "Barrita de Cereal", 10],
    [10, "Sanguchito de Miga", 15],
    [11, "Lata Coca-cola", 20],
    [12, "Doritos", 10]
]

#legajo y nombre

empleados = {
    1777: "Nahieli Insfran",
    1225: "Lautaro Dominguez",
    1300: "Pedro Chavez",
    1732: "Luna Cortes",
    1505: "Maximiliano Bertone",
    2222: "Fernanda Cartofield"
}

#clave del técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

#historial de pedidos
golosinasPedidas = []

# ---------------- MENU ----------------
opcion = ""

while opcion != "d":
    print()
    print("===== MÁQUINA EXPENDEDORA =====")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar máquina")

    opcion = input("Elegí una opción: ").lower()

    if opcion == "a":
        legajo = input("Ingresá tu legajo: ")

        if legajo.isdigit() and int(legajo) in empleados:
            print("Bienvenido/a,", empleados[int(legajo)])
            terminado = False

            while terminado == False:
                codigo = input("Ingresá el código de la golosina (o escribí salir): ").lower()

                if codigo == "salir":
                    terminado = True
                elif codigo.isdigit() and 1 <= int(codigo) <= len(golosinas):
                    fila = golosinas[int(codigo) - 1]

                    if fila[2] > 0:
                        fila[2] = fila[2] - 1
                        print("Retirá tu", fila[1], "¡Que la disfrutes!")

                        # ----- REGISTRO EN golosinasPedidas -----
                        encontrada = False
                        for pedida in golosinasPedidas:
                            if pedida[0] == fila[0]:
                                pedida[2] = pedida[2] + 1
                                encontrada = True

                        if encontrada == False:
                            golosinasPedidas.append([fila[0], fila[1], 1])
                        # ----------------------------------------

                        terminado = True
                    else:
                        print("Lo sentimos la golosina", fila[1], "no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
                else:
                    print("Código inválido, probá de nuevo")
        else:
            print("Usted no es un empleado de la empresa")

    elif opcion == "b":
        print()
        print("--- GOLOSINAS DISPONIBLES ---")
        for fila in golosinas:
            print(fila[0], "-", fila[1], "- Stock:", fila[2])

    elif opcion == "c":
        print()
        print("--- MODO TÉCNICO ---")
        clave1 = input("Ingresá la clave 1: ")
        clave2 = input("Ingresá la clave 2: ")
        clave3 = input("Ingresá la clave 3: ")

        if clave1 == clavesTecnico[0] and clave2 == clavesTecnico[1] and clave3 == clavesTecnico[2]:
            print("Acceso autorizado")
            codigo = input("Ingresá el código de la golosina a rellenar: ")

            if codigo.isdigit() and 1 <= int(codigo) <= len(golosinas):
                fila = golosinas[int(codigo) - 1]

                cantidad = input("Ingresá la cantidad a recargar: ")
                while cantidad.isdigit() == False or int(cantidad) <= 0:
                    print("La cantidad debe ser un número mayor a cero")
                    cantidad = input("Ingresá la cantidad a recargar: ")

                fila[2] = fila[2] + int(cantidad)
                print("Recarga exitosa. Ahora hay", fila[2], "unidades de", fila[1])
            else:
                print("Código inválido")
        else:
            print("No tiene permiso para ejecutar la función de recarga")

    elif opcion == "d":
        print()
        print("--- GOLOSINAS PEDIDAS ---")

        if len(golosinasPedidas) == 0:
            print("No se pidieron golosinas durante la ejecución")
        else:
            total = 0
            for pedida in golosinasPedidas:
                print(pedida[0], "-", pedida[1], "- Cantidad total pedida:", pedida[2])
                total = total + pedida[2]

            print()
            print("Total de golosinas pedidas:", total)

        print()
        print("Apagando máquina...")

    else:
        print("Opción inválida, intentá de nuevo")
