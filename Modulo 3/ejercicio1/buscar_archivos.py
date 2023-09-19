#EJERCICIO ruta y extensiones:

#Desarrollar un script buscar_archivos.py que reciba como argumentos la ruta a una carpeta y una extensión para buscar archivos dentro de ella. Luego debe mostrar los archivos que terminen con dicha extensión en la carpeta indicada.
# Por ejemplo:
# python buscar_archivos.py "C:\Ruta" .exe
# hola.exe
# chau.exe
# Si no se pasan los argumentos, el programa debe indicar que hubo un error.

import sys
import os

#pasamos los argumentos y validamos que haya la cantidad correcta
ruta = sys.argv[1]
extension = sys.argv[2]

if not ruta or not extension:
    print("Error: Debe ingresar una ruta y una extension")
    sys.exit()

#obtener una lista de archivos en la ruta

try:
    validar_ruta = os.listdir(ruta)
except FileNotFoundError:
    print("La ruta no existe")
    sys.exit()

for contenido in validar_ruta:
    if ruta.endswith(extension):
        print(contenido)
    else:
        print("No hay archivos con esa extension")
        sys.exit()
