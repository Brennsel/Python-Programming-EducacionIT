import sqlite3


dir = "B:\\Usuario\\Desktop\\Python developer\\Python-Programming\\Modulo 4\\"
conn = sqlite3.connect(dir + "database.sqlite")
cursor = conn.cursor()


def insertar():
    gente = (
        ("Pablo", 30),
        ("Jorge", 41),
        ("Pedro", 25)
    )

    try:
        for nombre, edad in gente:
            cursor.execute(f"INSERT INTO personas VALUES ('{nombre}', {edad})") # <-- SQL Injection
            #otra forma
            #cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad))
    except sqlite3.OperationalError:
        print("Error al insertar datos")


def consultar():
    try:
        cursor.execute("SELECT * FROM productos")
        personas_db = cursor.fetchall()
        return personas_db
    except sqlite3.OperationalError:
        print("La tabla no existe")

#funcion para que el usuario ingrese los datos

def ingreso_de_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # *** ESTAS LINEAS PERMITEN INYECCCION DE CODIGO SQL ***
    # cursor.executescript(f"INSERT INTO personas VALUES ('{nombre}', {edad})")
    # cursor.executescript("INSERT INTO personas VALUES ({}, {})".format(nombre, edad))
    # cursor.executescript("INSERT INTO personas VALUES ('" +nombre + "', " + str(edad) +")")

    cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad)) #forma correcta
    print("Los datos se ingresaron correctamente")


#ingreso_de_usuario()
print(consultar())

conn.commit()

conn.close() 









