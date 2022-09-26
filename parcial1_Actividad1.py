import tkinter
from tkinter import *

ventana = Tk()
ventana.title ("Parcial 1")
ventana.geometry("350x650")
ventana.configure(bg="black")

fuenteTitulo = ("Arial Black",16)
fuenteElmentos = ("Arial",14)
resultado = 0.0

#Operaciones
def promedio():
    suma = int(num1.get()) + int(num2.get()) + int(num3.get()) + int(num4.get()) + int(num5.get())
    salida = suma/5
    lbl_resultado["text"]=salida

def mayor():
    val1 = int(num1.get())
    val2 = int(num2.get())
    val3 = int(num3.get())
    val4 = int(num4.get())
    val5 = int(num5.get())

    if (val1!=val2) and (val1!=val3) and (val1!=val4) and (val1!=val5) and (val2!=val3) and (val2!=val4) and (val2!=val5) and (val3!=val4) and (val3!=val5) and (val4!=val5):
        if (val1>val2) and (val1>val3) and (val1>val4) and (val1>val5):
            lbl_resultado["text"] ="El número mayor es ",val1
        if (val2>val1) and (val2>val3) and (val2>val4) and (val2>val5):
            lbl_resultado["text"] ="El número mayor es ",val2
        if (val3>val2) and (val3>val1) and (val3>val4) and (val3>val5):
            lbl_resultado["text"] ="El número mayor es ",val3
        if (val4>val2) and (val4>val3) and (val4>val1) and (val4>val5):
            lbl_resultado["text"] ="El número mayor es ",val4
        if (val5>val2) and (val5>val3) and (val5>val4) and (val5>val1):
            lbl_resultado["text"] ="El número mayor es ",val5
    else:
        lbl_resultado["text"] ="La aplicación no contempla \nesta situación por lo que \nno puede indicar cual valor es el mayor."
    
def validar():
    suma = int(num1.get()) + int(num2.get()) + int(num3.get()) + int(num4.get()) + int(num5.get())
    multi = int(num1.get()) * int(num5.get())
    
    if (suma>multi):
        lbl_resultado["text"]= "La suma es mayor a la multiplicación \n",suma," ",multi
    if (suma==multi):
        lbl_resultado["text"]= "La suma es igual a la multiplicación \n",suma," ",multi
    if (suma<multi):
        lbl_resultado["text"]= "La suma es menor a la multiplicación \n",suma," ",multi

def salir():
    exit()
        
lbl_titulo = Label(ventana, text="PARCIAL", bg="yellow", font= fuenteTitulo)
lbl_titulo.pack(fill = tkinter.X)

lbl_valor1 = Label(ventana, text="Valor 1", bg="black", foreground="red", font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
num1 = Entry(ventana, font= fuenteElmentos)
num1.pack(fill = tkinter.X, pady=3)

lbl_valor1 = Label(ventana, text="Valor 2", bg="black", foreground="red", font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
num2 = Entry(ventana, font= fuenteElmentos)
num2.pack(fill = tkinter.X, pady=3)

lbl_valor1 = Label(ventana, text="Valor 3", bg="black", foreground="red", font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
num3 = Entry(ventana, font= fuenteElmentos)
num3.pack(fill = tkinter.X, pady=3)

lbl_valor1 = Label(ventana, text="Valor 4", bg="black", foreground="red",  font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
num4 = Entry(ventana, font= fuenteElmentos)
num4.pack(fill = tkinter.X, pady=3)

lbl_valor1 = Label(ventana, text="Valor 5", bg="black", foreground="red", font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
num5 = Entry(ventana, font= fuenteElmentos)
num5.pack(fill = tkinter.X, pady=3)

btn_promedio = Button(ventana, text="Promedio", font= fuenteElmentos, bg="skyblue", command= promedio)
btn_promedio.pack(fill = tkinter.X, pady=3)

btn_mayor = tkinter.Button(ventana, text="Mayor", font= fuenteElmentos, bg="skyblue", command= mayor)
btn_mayor.pack(fill = tkinter.X, pady=3)

btn_validar = tkinter.Button(ventana, text="Validar", font= fuenteElmentos, bg="skyblue", command= validar)
btn_validar.pack(fill = tkinter.X, pady=3)

lbl_resultado = tkinter.Label(ventana, text="Resultado", bg="black", foreground="red",  font= fuenteElmentos)
lbl_resultado.pack(fill = tkinter.X, pady=3)

btn_salir = tkinter.Button(ventana, text="Salir", font= fuenteElmentos, bg="red", command= salir)
btn_salir.pack(fill = tkinter.X, pady=3)

ventana.mainloop()