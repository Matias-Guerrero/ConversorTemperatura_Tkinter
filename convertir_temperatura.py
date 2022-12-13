import tkinter as tk

def convertirTemperatura():

    global sinEtiquetas
    
    try:
        temperaturaCelcius = float(temperatura.get())
    except:
        etiquetaKelvin.pack_forget()
        etiquetaFahrenheit.pack_forget()

        sinEtiquetas = True

        etiquetaInvalida.pack(
            fill="both",
            expand=True
        )

        return

    try:
        if sinEtiquetas == True:
            etiquetaInvalida.pack_forget()

            etiquetaKelvin.pack(
                fill="both",
                expand=True
            )
            etiquetaFahrenheit.pack(
                fill="both",
                expand=True
            )
    except:
        sinEtiquetas = False

    temperaturaKelvin = temperaturaCelcius + 273.15
    temperaturaFahrenheit = temperaturaCelcius * 1.8 + 32

    etiquetaKelvin.config(text=f"Temperatura en K: {temperaturaKelvin}")
    etiquetaFahrenheit.config(text=f"Temperatura en °F: {temperaturaFahrenheit}")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("500x600")

temperatura = tk.StringVar(ventana)

etiquetaCelsius = tk.Label(
    ventana,
    text="Ingrese Temperatura en °C:",
    fg="white",
    bg="black",
    justify="center"
)

etiquetaCelsius.pack(
    fill="both",
    expand=True
)

entradaCelsius = tk.Entry(
    ventana,
    font=("Courier", 14),
    justify="center",
    textvariable=temperatura
)

entradaCelsius.pack(
    fill="both",
    expand=True
)

botonConvertir = tk.Button(
    ventana,
    text="Convertir",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="white",
    command=convertirTemperatura
)

botonConvertir.pack(
    fill=tk.BOTH,
    expand=True
)

etiquetaKelvin = tk.Label(
    ventana,
    text="Temperatura en K: n/a",
    fg="white",
    bg="black",
    justify="center"
)

etiquetaKelvin.pack(
    fill="both",
    expand=True
)

etiquetaFahrenheit = tk.Label(
    ventana,
    text="Temperatura en °F: n/a",
    fg="white",
    bg="black",
    justify="center"
)

etiquetaFahrenheit.pack(
    fill="both",
    expand=True
)

etiquetaInvalida = tk.Label(
    ventana,
    text="Entrada invalida\nIntentelo nuevamente!!",
    fg="white",
    bg="black",
    justify="center"
)

ventana.mainloop()