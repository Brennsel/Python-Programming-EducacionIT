import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

#Funcion boton
def funcion_boton(nombre):
    print(nombre, "Botón presionado")
    boton.config(text="Botón presionado") #Cambia el texto del boton


#Funcion caja de texto
def imprime_texto():
    print(caja.get())


def agregar_texto():
    caja.insert(0, "Agregado") #Inserta texto en la caja de texto


def elimina_chars():
    caja.delete(0, 5) #Elimina caracteres de la caja de texto de 0 a 4 inclusive


def elimina_texto():
    caja.delete(0, tk.END) #Elimina todo el texto de la caja de texto


def imprime_seleccion():
    print(lista.curselection()) #Devuelve el indice del elemento seleccinado
    print(lista.get(lista.curselection())) #Devuelve el elemento seleccionado


def imprime_estado():
    print(estado_caja.get()) #Devuelve el estado del checkbox
    #estado_caja.set(True) #Cambia el estado del checkbox a True


def nuevo():
    print("Nuevo Archivo")


def eliminar():
    print("Archivo eliminado")


def acerca_de():
    print("Acerca de")



ventana = tk.Tk()

ventana.title("Mi aplicación")

#Barra de menu
menu = tk.Menu()
menu_archivo = tk.Menu(menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Eliminar", command=eliminar)
menu_ayuda = tk.Menu(menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu.add_cascade(label="Ayuda", menu=menu_ayuda)




ventana.config(width=600, height=600)

#Botones
#FORMA 1:
# boton1 = ttk.Button(text="Botón 1", command=funcion_boton)
# boton1.place(x=50, y=10)

#FORMA 2:
boton = ttk.Button(text="Soy un boton", command=lambda:funcion_boton("Brenda"))
#boton.place(x=50, y=10)
boton.grid(row=0, column=0)


#Cajas de texto
#FORMA 1 (ttk):
caja = ttk.Entry()
caja.grid(row=1, column=0)
#caja.place(x=10, y=50)
boton2 = tk.Button(text="Obtener texto", command=imprime_texto)
boton2.grid(row=1, column=1)
#boton2.place(x=150, y=45)
agrega = tk.Button(text="Agregado", command=agregar_texto)
agrega.grid(row=3, column=0)
#agrega.place(x=10, y=80)
elimina_5 = tk.Button(text="Elimina 5", command=elimina_chars)
elimina_5.grid(row=3, column=1)
#elimina_5.place(x=80, y=80)
elimina_todo = tk.Button(text="Eliminar todo", command=elimina_texto)
elimina_todo.grid(row=3, column=2)
#elimina_todo.place(x=145, y=80)


# #Etiqueta
# imagen = PhotoImage(file="B:\Usuario\Desktop\Python developer\Python-Programming\Modulo 6\drive.png")
# label = tk.Label(ventana, image=imagen)
# label.grid(row=4, column=2)
# label.place(x=90, y=120)


#Listbox
lista = tk.Listbox()
lista.insert(0, "Python" , "C++", "C#" "Java")
lista.grid(row=4, column=0)
#lista.place(x=10, y=250)
boton3 = tk.Button(text="Lista", command=imprime_seleccion)
boton3.grid(row=4, column=1)
#boton3.place(x=10, y=220)

#Combobox
lista_desplegable = ttk.Combobox(
    values=[
        "VSCode",
        "VSCommunity",
        "PyCharm",
        "Eclipse"
    ]
)
lista_desplegable.grid(row=5, column=0, columnspan=2)
#lista_desplegable.place(x=140, y=200)


#Checkbox
#estado_caja = tk.BooleanVar() #Se utiliza para que devuelva valores booleanos
estado_caja = tk.StringVar(value="Sin") #Se utiliza para que devuelva valores personalizados
checkbutton = ttk.Checkbutton(text="Con/Sin Airbag", variable=estado_caja, onvalue="Con", offvalue="Sin")
checkbutton.grid(row=5, column=2)
# checkbutton.place(x=140, y=230)
boton4 = tk.Button(text="Estado", command=imprime_estado)
boton4.grid(row=6, column=2)
#boton4.place(x=150, y=260)

#Cuadros de dialogo
#import tkinter.messagebox as mbox
#essagebox.showinfo(title="Titulo", message="Mensaje")

# Showwarnig - Muestra un mensaje de advertencia
# messagebox.showwarning(title="Advertencia", message="Esto es una advertencia!!!")

# Showerror - Muestra un mensaje de error
#messagebox.showerror(title="Error", message="Algo salio mal!!!")

# Askquestion - Muestra un mensaje de pregunta si=true no=false
# respuesta = messagebox.askquestion(title="Confirmacion", message="¿Desea cerrar el programa?")
# if respuesta:
#     ventana.destroy()

#Askretrycancel - Muestra un mensaje de pregunta si=true no=false
# respuesta = messagebox.askretrycancel(title="Reintentar", message="No se puede conectar")



ventana.mainloop()

#Ejercicio de practica
