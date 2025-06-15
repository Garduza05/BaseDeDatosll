import tkinter as tk
from tkinter import*

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("sistema")
ventana.resizable(False, False)
ventana = Frame(height=250,width=350,bg="white")
ventana.pack(padx=95,pady=85)

#Agregar un campo de texto para ingresar el nombre del cliente
etiqueta_cliente = tk.Label(ventana,text="Nombre del cliente:")
etiqueta_cliente.pack()
entrada_cliente = tk.Entry(ventana)
entrada_cliente.pack()

#Agregar un boton para confirmar la venta
boton_confirmar = tk.Button(ventana, text="Confirmar venta",
command=lambda: print("venta realizada"))
boton_confirmar.pack()

ventana.mainloop()