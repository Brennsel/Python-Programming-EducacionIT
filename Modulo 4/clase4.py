""" 
# MySQL <-- mysql-connector-python, PyMySQL, MySQLdb
# PostgreSQL --> psycopg, pg8000
# SQLite <-- sqlite3
# SQL Server --> pymssql, pyodbc
# Oracle --> cx_Oracle

# SQLite

# Browser --> https://sqlitebrowser.org

import sqlite3

# Variable donde guarda la BBDD
dir = r"B:\Usuario\Desktop\Python developer\Python-Programming\Modulo 4\"

# Crear una conexión con la BBDD
conn = sqlite3.connect(dir + "database.sqlite")

# Crear cursor
cursor = conn.cursor()

# Correr código SQL con el método execute()
try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")
except sqlite3.OperationalError:
    print("La tabla ya existe")

# Realizamos un commit() para confirmar los cambios
conn.commit()

# Finalizamos la conexión
conn.close() """

#///////////////////////////////////////////////////////////////////////////////
#MySQL (Structured Query Language - Lenguaje de Consulta Estructurado)

"""
abrir XAMPP
Para crear un usuario, abrir un CMD, ir donde esta instalado XAMPP

cd C:\xampp\mysql\ bin
mysql -u root

1 - Crear un usuario
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'password';

2 - Concederle privilegios
GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'localhost';

3 - Actualizamos para que los cambios tengan efecto
FLUSH PRIVILEGES;

4 - Crear una base de datos
CREATE DATABASE nombre_db;

5 - Dar privilegios al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON nombre_db.* TO 'usuario'@'localhost';

6 - Actualizamos para que los cambios tengan efecto
FLUSH PRIVILEGES;

instalamos pymysql
pip install pymysql
"""

import pymysql

conn = pymysql.connect(
    host="Localhost",
    port=3306,
    user="brenda",
    password="root",
    db="digitalers" 
)

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE personas (nombre VARCHAR(50), edad INT)")
except pymysql.OperationalError:
    print("La tabla ya existe")


gente = (
    ("Pablo", 30),
    ("Jorge", 41),
    ("Pedro", 25)
)

for nombre, edad in gente:
     cursor.execute(f"INSERT INTO personas VALUES (%s, %s)", {nombre, edad})


try:
    cursor.execute("SELECT * FROM personas")
except pymysql.OperationalError:
    print("Error la consulta es erronea")

conn.commit()

cursor.execute("SELECT * FROM personas")
datos = cursor.fetchall()
print(datos)

conn.close()

#VULNERABILIDAD EN SQL

conn = pymysql.connect(
    host="Localhost",
    port=3306,
    user="brenda",
    password="root",
    db="digitalers",
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

cursor = conn.cursor()

def ingreso_de_datos():
    try:
        cursor.execute("CREATE TABLE personas (nombre VARCHAR(50), edad INT)")
    except pymysql.OperationalError:
        print("La tabla ya existe")

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    cursor.execute(f"INSERT INTO personas VALUES ('{nombre}', {edad})") # <-- SQL Injection
    conn.commit()
    print("Los datos se ingresaron correctamente")
    

def consultar_datos():
    try:
        cursor.execute("SELECT * FROM personas")
    except pymysql.OperationalError:
        print("Error la consulta es erronea")

    datos = cursor.fetchall()
    print(datos)
    conn.close()

ingreso_de_datos()


#///////////////////////////////////////////////////////////////////////////////
""" Ejercicio 2: Administrar productos v.2

Realizar un programa que permita agregar nuevos productos a una base de datos del tipo MySQL a través de la consola. Se deberá solicitar para cada producto un id (numérico entero), un nombre (texto) y un precio (numérico entero). En el caso de los datos numéricos, volver a preguntar si el valor ingresado por el usuario es incorrecto. 

Para acompañar al programa, hacer un menú como el siguiente:

Menú

1 – Agregar Productos

2 – Ver productos

3 – Salir

La opción de agregar productos será la que despliegue la entrada de datos.

La opción ver productos mostrará todos los productos cargados en la tabla.

La opción de salir nos permite salir del programa.

Recomendamos:

Los mismos consejos para el ejercicio 2 del laboratorio anterior, la versión 1 con sqlite, pero teniendo en cuenta que ahora estamos trabajando con MySQL.

Esta vez la base de datos ya estará creada en el servidor por nosotros. """




