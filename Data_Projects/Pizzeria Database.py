# Importar librerias tkinter y PIL para la configuración de la interfaz gráfica
# Importar PIL para configurar el fondo de la interfaz con archivo .jpg
# Importar uuid para la generación de códigos con estándar uuid4 para la clasificación de datos 
# Importar json para el manejo y almacenamiento de datos
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import uuid as codigos
import json

#Declarar variables globales para mejor funcionamiento del programa

global listaDatos, posicionActual

#Declarar lista vacía para inicializar la recopilación de datos
listaDatos = []

#Configuración interfaz:
#Ventana Principal
interfaz = Tk()
interfaz.title("Pizzeria Pizzato")
interfaz.geometry("2120x1080")
imagenFondoInterfaz = ImageTk.PhotoImage(Image.open("fondo.jpg"))
fondoInterfaz = Label(interfaz, image = imagenFondoInterfaz).place(x = 0, y = 0)

#Títulos ingreso información

marcoInformacion = LabelFrame(interfaz, text = "Información cliente", bg = "PaleTurquoise4", font = ("ArialBlack", 14))
marcoInformacion.grid(row=0,column=0,rowspan=5,columnspan=4)

barraIngresoID = Label(marcoInformacion,            anchor = "w",           width = 24,
                       height = 1,                  relief = "ridge",       text = "ID",
                       font = ("Consolas", 14)   ).grid(row=1, column=0)

barraIngresoNombre = Label(marcoInformacion,            anchor = "w",           width = 24,
                           height = 1,                  relief = "ridge",       text = "Nombre",
                           font = ("Consolas", 14)   ).grid(row=2, column=0)

barraIngresoApellidos = Label(marcoInformacion,            anchor = "w",           width = 24,
                              height = 1,                  relief = "ridge",       text = "Apellidos",
                              font = ("Consolas", 14)   ).grid(row=3, column=0)

barraIngresoTelefono = Label(marcoInformacion,            anchor = "w",           width = 24,
                             height = 1,                  relief = "ridge",       text = "Teléfono",
                             font = ("Consolas", 14)   ).grid(row=4, column=0)

barraIngresoTamaño = Label(marcoInformacion,            anchor = "w",           width = 24,
                           height = 1,                  relief = "ridge",       text = "Tamaño",
                           font = ("Consolas", 14)   ).grid(row=5, column=0)

barraIngresoIngredientes = Label(marcoInformacion,            anchor = "w",           width = 24,
                                 height = 1,                  relief = "ridge",       text = "Ingredientes",
                                 font = ("Consolas", 14)   ).grid(row=6, column=0)

#Creación códigos unicos
crearID = StringVar()
crearID.set(codigos.uuid4())

#Ingreso información
entradaID = Label(marcoInformacion,       anchor = "w",     height = 1,                  
                  relief = "ridge",       textvariable = crearID,      font = ("ArialBlack", 14))
entradaID.grid(row = 1, column = 1)

entradaNombre = Entry(marcoInformacion,width=30,borderwidth=2,fg="black",font=('Consolas',14))
entradaNombre.grid(row=2, column=1,columnspan=2)
entradaApellidos = Entry(marcoInformacion,width=30,borderwidth=2,fg="black",font=('Consolas',14))
entradaApellidos.grid(row=3, column=1,columnspan=2)
entradaTelefono = Entry(marcoInformacion,width=30,borderwidth=2,fg="black",font=('Consolas',14))
entradaTelefono.grid(row=4, column=1,columnspan=2)
entradaTamaño = Entry(marcoInformacion,width=30,borderwidth=2,fg="black",font=('Consolas',14))
entradaTamaño.grid(row=5, column=1,columnspan=2)
entradaIngredientes = Entry(marcoInformacion,width=30,borderwidth=2,fg="black",font=('Consolas',14))
entradaIngredientes.grid(row=6, column=1,columnspan=2) 

#Listado Datos

datos = ttk.Treeview(interfaz, columns=(1,2,3,4,5,6),show="headings",height="16")
datos.grid(row=11,column=0, rowspan=16,columnspan=4)

datos.heading(1, text = "ID", anchor = "center")
datos.heading(2, text = "Nombre", anchor = "center")
datos.heading(3, text = "Apellidos", anchor = "center")
datos.heading(4, text = "Teléfono", anchor = "center")
datos.heading(5, text = "Tamaño", anchor = "center")
datos.heading(6, text = "Ingredientes", anchor = "center")

datos.column("#1", anchor = "w", width = 270, stretch = True)
datos.column("#2", anchor = "w", width = 215, stretch = False)
datos.column("#3", anchor = "w", width = 215, stretch = False)
datos.column("#4", anchor = "w", width = 215, stretch = False)
datos.column("#5", anchor = "w", width = 215, stretch = False)
datos.column("#6", anchor = "w", width = 235, stretch = False)

#Funciones interfaz
#Cargar datos desde el archivo json
def cargarArchivoJson ():
    global listaDatos
    with open("listadoClientes.json", "r") as file_handler:
        listaDatos = json.load(file_handler)
    file_handler.close
    print('El archivo ha sido leído')

#Actualizar la data almacenada en el archivo json
def actualizarArchivoJson():
    global listaDatos
    with open("listadoClientes.json", "w") as file_handler:
        json.dump(listaDatos, file_handler, indent=4)
    file_handler.close
    print('EL archivo ha sido actualizado')

#Eliminar cliente del archivo json
def eliminarDatosLista():
    for item in datos.get_children():
        datos.delete(item)

#Almacenar datos ingresados en un diccionario
def cargarDatosJson():
    global listaDatos

    eliminarDatosLista()

    filaActual=1

    for key in listaDatos:
        idActual = key["ID"]
        Nombre = key["Nombre"]
        Apellidos = key["Apellidos"]
        Telefono = key["Telefono"]
        Tamaño = key["Tamaño"]
        Ingredientes = key["Ingredientes"]
        datos.insert('',index='end',iid=filaActual,text="",
               values=(idActual, Nombre, Apellidos, Telefono, Tamaño, Ingredientes))    
        filaActual = filaActual+1

#Limpiar espacios de ingreso de datos
def limpiarCliente():
    entradaNombre.delete(0,END)
    entradaApellidos.delete(0,END)
    entradaTelefono.delete(0,END)
    entradaTamaño.delete(0,END)
    entradaIngredientes.delete(0,END)
    entradaID.configure(text="")
    entradaNombre.focus_set()
    crearID.set(codigos.uuid4())
    cambiarColorCeldas("#FFFFFF")

#Hallar posición actual del cliente 
def filaListaDatos(idActual):
    global listaDatos
    entrada     = 0
    valido   = False

    for rec in listaDatos:
        if rec["ID"] == idActual:
            valido = True
            break
        entrada = entrada+1

    if(valido==True):
        return(entrada)

    return(-1)

#Cambiar color celdas en caso de error
def cambiarColorCeldas(color_nuevo):
    entradaNombre.config(bg=color_nuevo)
    entradaApellidos.config(bg=color_nuevo)
    entradaTelefono.config(bg=color_nuevo)
    entradaTamaño.config(bg=color_nuevo)
    entradaIngredientes.config(bg=color_nuevo)

#Cambiar estado botones según función elegida
def cambiarEstadoActivo(estado):
    if estado == 'Edit':
        botonActualizar["state"]="normal"
        botonEliminar["state"]="normal"
        botonAñadir["state"]="disabled"
    elif estado=='Cancel':
        botonActualizar["state"]="disabled"
        botonEliminar["state"]="disabled"
        botonAñadir["state"]="disabled"
    else:
        botonActualizar["state"]="disabled"
        botonEliminar["state"]="disabled"
        botonAñadir["state"]="normal"

#Cargar datos ingresados en diccionario
def cargarDatosFila(_tuple):
    if len(_tuple)==0:
        return;

    crearID.set(_tuple[0]);
    entradaNombre.delete(0,END)
    entradaNombre.insert(0,_tuple[1])
    entradaApellidos.delete(0,END)
    entradaApellidos.insert(0,_tuple[2])
    entradaTelefono.delete(0,END)
    entradaTelefono.insert(0,_tuple[3])
    entradaTamaño.delete(0,END)
    entradaTamaño.insert(0,_tuple[4])
    entradaIngredientes.delete(0,END)
    entradaIngredientes.insert(0,_tuple[5])

#Cancelar acción elegida
def Cancelar():
    limpiarCliente()
    cambiarEstadoActivo('New')

#Imprimir en pantalla datos cliente
def imprimirEntradasCliente():
   global listaDatos

   for rec in listaDatos:
        print(rec)

   entradaNombre.focus_set();

#Generar diccionario nuevo para subir al archivo json
def agregarCliente():
    id = crearID.get()
    Nombre = entradaNombre.get()
    Apellidos = entradaApellidos.get()
    Telefono = entradaTelefono.get()
    Tamaño = entradaTamaño.get()
    Ingredientes = entradaIngredientes.get()
    if len(Nombre)==0:
        cambiarColorCeldas("#FFB2AE")
        return

    seleccionOperacion('Añadir',id,Nombre,Apellidos,Telefono,Tamaño,Ingredientes)

#Actualizar datos cliente en archivo json
def actualizarCliente():
    id = crearID.get()
    Nombre = entradaNombre.get()
    Apellidos = entradaApellidos.get()
    Telefono = entradaTelefono.get()
    Tamaño = entradaTamaño.get()
    Ingredientes = entradaIngredientes.get()

    if len(Nombre) == 0:
        cambiarColorCeldas("#FFB2AE")
        return
    seleccionOperacion("Actualizar", id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes)

#Eliminar información cliente del archivo json
def eliminarCliente():
    id = crearID.get()
    seleccionOperacion('Eliminar',id,None,None,None,None,None)

#Seleccionar acción a realizar en el archivo json
def seleccionOperacion(comando, id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes):
    global listaDatos

    if comando == "Actualizar":
        row = filaListaDatos(id)
        if row >= 0:
            dict = {"ID":id, "Nombre":Nombre, 
                    "Apellidos":Apellidos, "Telefono":Telefono, "Tamaño":Tamaño, "Ingredientes":Ingredientes}
            listaDatos[row]=dict

    elif comando == "Añadir":
        dict = {"ID":id, "Nombre":Nombre, 
                "Apellidos":Apellidos, "Telefono":Telefono, "Tamaño":Tamaño, "Ingredientes":Ingredientes}
        listaDatos.append(dict)

    elif comando == "Eliminar":
        row = filaListaDatos(id)
        if row >= 0:
            del listaDatos[row];

    actualizarArchivoJson();
    cargarDatosJson();
    limpiarCliente();

#Mostrar ultima selección del mouse
def mostrarSeleccionActual(event):
    posicionActual = datos.selection()[0]
    ultimoCliente = (datos.item(posicionActual,'values'))
    cargarDatosFila(ultimoCliente)
    cambiarEstadoActivo("Edit")

datos.bind("<ButtonRelease>",mostrarSeleccionActual)

#Generar botones en pantalla
espacioBotonesOperaciones = LabelFrame(interfaz, text = "", bg = "PaleTurquoise4", font = ("Consolas", 14))
espacioBotonesOperaciones.grid(row=10,column=0,columnspan=6)
botonMostrarenTerminal = Button(espacioBotonesOperaciones, text = "Mostrar", padx = 20, pady = 10, command = imprimirEntradasCliente)
botonMostrarenTerminal.pack(side = LEFT)
botonAñadir = Button(espacioBotonesOperaciones, text = "Añadir", padx = 20, pady = 10, command = agregarCliente)
botonAñadir.pack(side = LEFT)
botonActualizar = Button(espacioBotonesOperaciones, text = "Actualizar", padx = 20, pady = 10, command = actualizarCliente)
botonActualizar.pack(side = LEFT)
botonEliminar = Button(espacioBotonesOperaciones, text = "Eliminar", padx = 20, pady = 10, command = eliminarCliente)
botonEliminar.pack(side = LEFT)
botonCancelar = Button(espacioBotonesOperaciones,text="Cancelar",padx=18,pady=10,command=Cancelar)
botonCancelar.pack(side=LEFT)
botonSalir = Button(espacioBotonesOperaciones, text = "Salir", padx = 20, pady = 10, command = interfaz.quit)
botonSalir.pack(side = LEFT)

cargarArchivoJson()
cargarDatosJson()

#Inicializar programa
entradaNombre.focus_set();
interfaz.mainloop()