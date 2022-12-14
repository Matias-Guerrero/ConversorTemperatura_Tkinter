import tkinter as tk

""" 
===================
Funciones a Ocupar:
===================
"""

def convertirTemperatura():

    try:
        temperaturaInicial = float(temperaturaEntrada.get())
    except:
        salida.delete(0, tk.END)
        salida.insert(0, "Entrada No Valida!")
        return

    salida.delete(0, tk.END)

    seleccionEntrada = lista1.curselection()
    seleccionSalida = lista2.curselection()

    if seleccionEntrada == () or seleccionSalida == ():
        salida.delete(0, tk.END)
        salida.insert(0, "Seleccione Entrada Y Salida")
        return
    
    if seleccionEntrada[0] == 0:

        if seleccionSalida[0] == 0:
            salida.delete(0, tk.END)
            salida.insert(0, f"{temperaturaInicial}°")
        
        if seleccionSalida[0] == 1:
            temperaturaFahrenheit = temperaturaInicial * 1.8 + 32
            salida.delete(0, tk.END)
            salida.insert(0, f"{temperaturaFahrenheit}°")

        if seleccionSalida[0] == 2:
            temperaturaKelvin = temperaturaInicial + 273.15
            salida.delete(0, tk.END)
            salida.insert(0, f"{temperaturaKelvin}°")


    # temperaturaKelvin = temperaturaCelcius + 273.15
    # temperaturaFahrenheit = temperaturaCelcius * 1.8 + 32

def onEnter(event):
    convertirTemperatura()

def clearTextInput():
    entrada.delete(0, tk.END)

def onClick(event):
    clearTextInput()

""" 
==========================
Creacion Ventana Principal
========================== 
"""

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Conversor de T°")
ventanaPrincipal.geometry("500x300")
ventanaPrincipal.resizable(0, 0)

ventanaPrincipal.columnconfigure(0, weight=1)
ventanaPrincipal.columnconfigure(1, weight=1)

ventanaPrincipal.rowconfigure(0, weight=3)
ventanaPrincipal.rowconfigure(1, weight=3)
ventanaPrincipal.rowconfigure(2, weight=1)
ventanaPrincipal.rowconfigure(3, weight=3)

""" 
================
Variables a Usar
================ 
"""

lista = ("Grados Celsius", "Grados Fahrenheit", "Grados Kelvin")
var = tk.Variable(value=lista)

temperaturaEntrada = tk.StringVar(ventanaPrincipal)

""" 
==============
Widgets a Usar
============== 
"""

etiqueta1 = tk.Label(
    ventanaPrincipal,
    text="Entrada:",
    fg="white",
    bg="red",
    font=("Courier", 14),
    justify="center"
)

lista1 = tk.Listbox(
    ventanaPrincipal,
    listvariable=var,
    height=3,
    font=("Courier", 10),
    exportselection=False
)

etiqueta2 = tk.Label(
    ventanaPrincipal,
    text="Salida:",
    fg="white",
    bg="red",
    font=("Courier", 14),
    justify="center"
)

lista2 = tk.Listbox(
    ventanaPrincipal,
    listvariable=var,
    height=3,
    font=("Courier", 10),
    exportselection=False
)

entrada = tk.Entry(
    ventanaPrincipal,
    font=("Courier", 10),
    justify="center",
    textvariable=temperaturaEntrada
)

entrada.bind('<Return>', onEnter)
entrada.bind('<Button-1>', onClick)

salida = tk.Entry(
    ventanaPrincipal,
    font=("Courier", 10),
    justify="center",
)

botonConvertir = tk.Button(
    ventanaPrincipal,
    text="Convertir",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="white",
    command=convertirTemperatura
)

""" 
==========================
Posicionamiento de Widgets
========================== 
"""

etiqueta1.grid(
    padx=5,
    pady=5,
    row=0,
    column=0,
    sticky=tk.NSEW
)

lista1.grid(
    padx=5,
    pady=5,
    row=1,
    column=0,
    sticky=tk.NSEW
)

entrada.grid(
    padx=5,
    pady=5,
    row=2,
    column=0,
    sticky=tk.NSEW
)

etiqueta2.grid(
    padx=5,
    pady=5,
    row=0,
    column=1,
    sticky=tk.NSEW
)

lista2.grid(
    padx=5,
    pady=5,
    row=1,
    column=1,
    sticky=tk.NSEW
)

salida.grid(
    padx=5,
    pady=5,
    row=2,
    column=1,
    sticky=tk.NSEW
)

botonConvertir.grid(
    padx=5,
    pady=5,
    row=3,
    column=0,
    columnspan=2,
    sticky=tk.NSEW
)

ventanaPrincipal.mainloop()