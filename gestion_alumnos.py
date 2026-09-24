#----------------------- TP GRUPAL READ ----------------------------






#-------------------Ver Alumnos--------------------

with open("TP GRUPAL READ/alumnos.txt") as archivo:
    for linea in archivo:
        print(linea.replace(";"," | "))

#-------------------Agregar Alumno--------------------

