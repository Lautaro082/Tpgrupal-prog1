#Integrantes:
#---Nahieli Celeste Insfran---
#--Lautaro Nicolas Dominguez--

#========================
#         Listas
#========================

#========================
#       Ejercicio 1
#========================

num_list = []

for i in range(5):
    print(f"Ingrese 5 Numeros, vuelta {i+1}")
    user = int(input("Ingrese el numero: "))
    num_list.append(user)

suma = sum(num_list)
print(suma)

#========================
#       Ejercicio 2
#========================

lista = []

for i in range(7):
    print(f"Ingrese 7 Numeros, vuelta {i+1}")
    user = int(input("Ingrese el numero: "))
    lista.append(user)
print(f"El numero maximo es: {max(lista)}")
print(f"El numero minimo es: {min(lista)}")

#========================
#       Ejercicio 3
#========================

lista2 = []

user = input("Ingrese cualquier frase o palabra: ")

for character in user:
    lista2.append(character)
lista2.reverse()
print(*lista2)

#========================
#       Ejercicio 4
#========================

lista_num = []

for i in range(7):
    print(f"Ingrese 7 Numeros, vuelta {i+1}")
    user = int(input("Ingrese el numero: "))
    lista_num.append(user)
pares = [x for x in lista_num if x % 2 == 0]
impares = [x for x in lista_num if x % 2 != 0]
print(pares)
print(impares)

#========================
#       Ejercicio 5
#========================

numlist = ["12","25","5","86","4"]
resultado = []
usrs = int(input("Ingrese un numero para multiplicar la lista: "))

for elementos in numlist:
    multiplicacion = int(elementos)*usrs
    resultado.append(multiplicacion)

print(*resultado)

#========================
#       Ejercicio 6
#========================

list_num = []

for i in range(7):
    print(f"Ingrese 7 Numeros, vuelta {i+1}")
    user = int(input("Ingrese el numero: "))
    list_num.append(user)
for i in range(7):
    listas_out_duplex = set(list_num)
print(listas_out_duplex)

#========================
#       Ejercicio 7
#========================

from statistics import mean
list_num2 = []

for i in range(7):
    print(f"Ingrese 7 Numeros, vuelta {i+1}")
    user = int(input("Ingrese el numero: "))
    list_num2.append(user)

list2 = mean(list_num2)
print(f"el promedio es: {list2:.2f}")

#========================
#       Ejercicio 8
#========================

lista3 = ["1","1","5","4","66","45","5","45"]
offdupl = []
ondupl = []

for ids in lista3:
    if ids not in offdupl:
        offdupl.append(ids)
    else:
        ondupl.append(ids)
print(*ondupl)

#========================
#       Ejercicio 9
#========================

def es_primo(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True

entrada = input("ingrese los numeros separados por espacio: ")

lista_strings = entrada.split()
numeros = []

for x in lista_strings:
    numeros.append(int(x))

primos = []

for n in numeros:
    if es_primo(n):
        primos.append(n)

print("Los numeros primos son:")
print(primos)


#========================
#       Ejercicio 10
#========================

#Números
entrada = input("ingrese numeros separados por espacios: ")
numeros = [int(input(n) for n in entrada.split())]

#Indice a eliminar
indice = int(input(f"Ingrese el indice a eliminar (0 a {len(numeros) -1}):"))

#Final: validación
if 0 <= indice < len(numeros):
    eliminado = numeros.pop(indice)
    print(f"Elemento eliminado: {eliminado}")
    print("Lista final:", numeros)
else:
    print("Indice no valido.")

#========================
#       Ejercicio 11
#========================

#lista de numeros
entrada = input("Por favor, ingrese números separados por espacios: ")
numeros = [int(n) for n in entrada.splt()]

#pedir el numero a buscar
objetivo = int(input("Ingrese el número que desea contar: "))

#print final
cantidad = numeros.count(objetivo)
print(f"El número {objetivo} aparece {cantidad} veces en la lista.")

#========================
#       Ejercicio 12
#========================
 
#definir las listas solo de la misma longitud
lista1 = [10, 20, 30, 40]
lista2 = [5, 15, 25, 35]

lista_suma = []

#suma los elementos usando el índice
for i in range(len(lista1)):
    suma = lista1[i] + lista2[i]
    lista_suma.append(suma)

#print final
    print("lista 1:", lista1)
    print("lista 2:", lista2)
    print("Resultado de la suma:", lista_suma)

#========================
#       Ejercicio 13
#========================

#NumPy es una biblioteca fundamental de Python para la computación científica 
#y el manejo de grandes arrays y matrices multidimensionales.

#EJEMPLO:
import numpy as np

temperaturas = np.array([
    [14, 19, 16]
])

print("Temperaturas:")
print(temperaturas)

print("\nSuma de 2 grados:")
print(temperaturas + 2)

print("\nTemperatura más alta:")
print(np.max(temperaturas))


#========================
# Listas Bidimensionales
#========================

#========================
#       Ejercicio 1
#========================

def crear_matriz(filas, columnas):
    matriz = []
    contador = 1

    for i in range(filas):
        fila = []
        for i in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
    return matriz

#print final
mi_matriz = crear_matriz(3, 3)
print(mi_matriz)

#========================
#       Ejercicio 2
#========================
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma_total = 0
for fila in matriz:
    suma_total += sum(fila)

print("La suma total es: ", suma_total)

#========================
#       Ejercicio 3
#========================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    suma_fila = sum(matriz[i])
    print("Suma de la fila", i, ":", suma_fila)

#========================
#       Ejercicio 4
#========================

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

filas = len(matriz)
columnas = len(matriz[0])

transpuesta = []

for j in range(columnas):
    nueva_fila = []
    for i in range(filas):
        nueva_fila.append(matriz[i][j])
    transpuesta.append(nueva_fila)
    
print("Matriz transpuesta:", transpuesta)

#========================
#       Ejercicio 5
#========================

matriz = [
    [5, 12, 3],
    [8, 25, 1],
    [14, 7, 9]
]

#suponemos que el primer elemento es el mayor
mayor = matriz[0][0]

for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento

print("El valor más grande es:", mayor)


#========================
#       Ejercicio 6
#========================

matriz = [
    [1, 2, 3]
    [4, 5, 6]
]

escalar = int(input("Por favor, ingrese numero a multiplicar: "))

matriz_resultante = []

for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * escalar)
    matriz_resultante.append(nueva_fila)
    
print("Matriz resultante:")

#========================
#       Ejercicio 7
#========================

matriz = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]

numero = []

for i in range(len(matriz)):
    diagonal = matriz[i][i]
    numero.append(diagonal)
print(*diagonal)

#========================
#       Ejercicio 8
#========================

n = 4
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
            
    matriz.append(fila)

for fila in matriz:
    print(fila)

#========================
#       Ejercicio 9
#========================

n = 4
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
            
    matriz.append(fila)

for fila in matriz:
    print(fila)

#========================
#       Ejercicio 10
#========================

matriz = [
    [1, 2, 3],
    [2, 5, 4],
    [3, 4, 9]
]

es_simetrica = True
n = len(matriz)

for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False

if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz NO es simétrica")

#========================
#       Ejercicio 11
#========================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


matriz_girada = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


matriz_girada[0][0] = matriz[2][0]  
matriz_girada[0][1] = matriz[1][0]  
matriz_girada[0][2] = matriz[0][0]  

matriz_girada[1][0] = matriz[2][1]  
matriz_girada[1][1] = matriz[1][1]  
matriz_girada[1][2] = matriz[0][1]  

matriz_girada[2][0] = matriz[2][2]  
matriz_girada[2][1] = matriz[1][2]  
matriz_girada[2][2] = matriz[0][2]  


for fila in matriz_girada:
    print(fila)

#========================
#       Ejercicio 12
#========================

cadena_notas = "45, 88, -5, 92, 30, 110, 75, 60, 15"

# 1. Convertir la cadena en lista
lista_cadenas = cadena_notas.split(",")

aprobados = []
reprobados = []
suma_validas = 0
total_validas = 0

for item in lista_cadenas:
    nota = int(item.strip())
    
    if nota < 0 or nota > 100:
        continue
    
    if nota >= 60:
        aprobados.append(nota)
    else:
        reprobados.append(nota)
        
    suma_validas += nota
    total_validas += 1

promedio = suma_validas / total_validas if total_validas > 0 else 0

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio de notas válidas:", promedio)
print("Últimos 2 aprobados:", aprobados[-2:])

#========================
#       Ejercicio 13
#========================

tareas = []

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre de la tarea: ")
        if nombre in tareas:
            print("La tarea ya está registrada.")
        else:
            tareas.append(nombre)
            print("Tarea agregada con éxito.")

    elif opcion == "2":
        nombre = input("Ingresa el nombre de la tarea a eliminar: ")
        if nombre in tareas:
            tareas.remove(nombre)
            print("Tarea eliminada con éxito.")
        else:
            print("Advertencia: La tarea no existe en la lista.")

    elif opcion == "3":
        print(f"Total de tareas registradas: {len(tareas)}")
        print("Primeras tareas:", tareas[:3])

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")