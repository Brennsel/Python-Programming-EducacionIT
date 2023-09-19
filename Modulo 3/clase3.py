# CLASES Y OBJETOS

"""
class MiClase:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def imprimir_edad(self):
        print(self.edad)


mi_objeto = MiClase("Juan", 34)
mi_objeto.imprimir_edad()
"""

"""
class OperacionesMatematicas:
    def __init__(self, numero):
        self.numero = numero


    def sumar(self, nro2):
        self.numero += nro2
        print(self.numero)


    def restar(self, nro2):
        self.numero -= nro2
        print(self.numero)


    def multiplicar(self, nro2):
        self.numero *= nro2
        print(self.numero)


mi_objeto = OperacionesMatematicas(10)
mi_objeto.sumar(5)
mi_objeto.restar(4)
mi_objeto.multiplicar(2)
mi_objeto.sumar(3)

otro_objeto = OperacionesMatematicas(3)
otro_objeto.sumar(8)
"""

# ENCAPSULAMIENTO

# Getters, Setters y Del

"""
class Clase:
    def __init__(self):
        self.__atributo = "Atributo Oculto"

    
    def get_atributo(self): # Getter
        return self.__atributo
    

    def set_atributo(self, valor): # Setter
        self.__atributo = valor


    def eliminar_atributo(self): # Del
        del self.__atributo


    def __saludo_privado(self):
        print("Hola!!, este es un saludo privado")


    def saludo_publico(self):
        self.__saludo_privado()
"""

# HERENCIA

# La clase Base, padre o superclase que contiene métodos y atributos que otras clases van a heredar
# La clase Derivada, hija o subclase que va a hereder métodos y atributos del padre.

"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas


class ClaseA:
    def __init__(self):
        self.a = 1

    def mensaje(self):
        print("Mensaje de la Clase A")


class ClaseB:
    def __init__(self):
        self.a = 2

    def mensaje(self):
        print("Mensaje de la clase B")


class ClaseC(ClaseA, ClaseB):
    def mensaje(self):
        print("Mensaje clase C") # Sobreescritura
        super().mensaje()


mi_objeto = ClaseC()
mi_objeto.mensaje()
"""

# POLIMORFISMO

"""
class Perro:
    def sonido(self):
        return "Guau!"
    

class Gato:
    def sonido(self):
        return "Miau!"
    

def sonido_del_animal(animal):
    return animal.sonido()

perro = Perro()
gato = Gato()

print(sonido_del_animal(perro))
print(sonido_del_animal(gato))
"""

"""
import math

class Figura:
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio


    def calcular_area(self):
        return math.pi * self.radio ** 2
    

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        return self.base * self.altura
    

# Creo las instancias de las subclases
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Calcular el área de diferentes figuras usando polimorfismo
def calcular_y_mostrar_area(figura):
    area = figura.calcular_area()
    print(f"El área de la figura es: {area}")


calcular_y_mostrar_area(circulo)
calcular_y_mostrar_area(rectangulo)
"""

#ARGUMENTOS DE PROGRAMA

#Libreria sys - sys.argv (es una lista)
#Sirve en caso de ejecutar el programa desde la terminal

"""
import sys # Importo la librería sys

nombres = sys.argv[1:] # Guardo los argumentos en una lista

if nombres:
    print(f"Hola, {nombres}!!")
else:
    print("No indicaste ningún nombre!")
"""

#SISTEMA DE ARCHIVOS

#Libreria os - os.listdir() (es una lista)

import os # Importo la librería os

#FUNCION os.listdir() - Devuelve una lista con los archivos y carpetas que se encuentran en el directorio indicado

# dir = os.listdir() # Guardo los archivos y carpetas en una lista
# print(os.listdir(os.getcwd())) # Imprimo la lista
# print(dir) # Imprimo la lista

# #FUNCION os.path.exists() - Devuelve True si el archivo o carpeta existe
# exists = os.path.exists("clase3.py") # Guardo el resultado en una variable
# print(exists) # Imprimo el resultado

# #FUNCION os.mkdir() - Crea una carpeta en el directorio actual
# try:
#     os.mkdir("demo1.py") # Creo la carpeta
# except FileExistsError:
#     print("La carpeta ya existe!!")

# #FUNCION os.rmdir() - Elimina una carpeta en el directorio actual

# try:
#     os.rmdir("demo1.py")
#     print("Se elimino la carpeta")
# except FileNotFoundError:
#     print("La carpeta no existe!!")
# except OSError:
#     print("La carpeta no esta vacia!!")

# #FUNCION os.remove() - Elimina un archivo en el directorio actual

# try:
#     os.remove("B:\\Usuario\\Desktop\\Python developer\\Python-Programming\Modulo3\\demo1\\temporal.txt")
#     print("Se elimino el archivo")
# except FileNotFoundError:
#     print("El archivo no existe!!")

# #FUNCION os.rename() - Renombra un archivo o carpeta en el directorio actual

# try:
#     os.rename("demo1.py", "demo2.py")
#     print("Se renombro el archivo")
# except FileNotFoundError:
#     print("El archivo no existe!!")

# #FUNCION os.system() - Ejecuta un comando del sistema operativo
# os.system("dir") # Ejecuto el comando dir de Windows

# #FUNCION os.name - Devuelve el nombre del sistema operativo
# print(os.name) # Imprimo el nombre del sistema operativo

# #SHUTIL - Libreria para copiar, mover y eliminar archivos y carpetas

# import shutil # Importo la librería shutil

# # #shutil.copy() - Copia un archivo en el directorio actual

# # directorio = "temporal.txt"
# # shutil.copy(directorio + "temporal.txt", directorio + "temporal2.txt)


# #shutil.move() - Mueve un archivo en el directorio actual

# #shutil.rmtree() - Elimina una carpeta en el directorio actual

# shutil.rmtree("demo3.py")

# #Cuidado al borrar archivos y carpetas con Python, no se puede recuperar una vez borrado en la papelera de reciclaje

#-----------------------------------------------------------------

#EJECUCION DE COMANDOS

import subprocess # Importo la librería subprocess

subprocess.run("dir", shell=True) # Ejecuto el comando dir de Windows
