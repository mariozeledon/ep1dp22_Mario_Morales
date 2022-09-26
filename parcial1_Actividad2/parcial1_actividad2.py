from cgitb import text
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import pu
from Mixtos import Mixto
from Publicos import Publico
from Centros_educativos import Centro

#Crear la ventana
ventana = Tk()
ventana.title ("Parcial 1 Actividad 2")
ventana.geometry("1100x900")
tabla = ttk.Treeview(ventana, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))


listaMixtos = []
listaPublico = []
listaCentro = []

def guardarDatos(): 
    mixto = Mixto()
    publico = Publico()
    centro = Centro()   
    mixto.cant_hombres=int(txt_cant_hombres.get())
    mixto.cant_mujeres=int(txt_cant_mujeres.get())
    listaMixtos.append(mixto)
    publico = Publico()
    publico.fecha_creacion=txt_fecha.get()
    publico.tipo=txt_tipo.get()
    publico.descripcion=txt_descripcion.get()
    listaPublico.append(publico)
    centro.codigo=int(txt_codigo.get())
    centro.nombre=txt_nombre.get()
    centro.direccion=txt_direccion.get()
    centro.telefono=int(txt_telefono.get())
    centro.director=txt_director.get()
    centro.url=txt_url.get()
    listaCentro.append(centro)
    generarTabla() 

'''----------------------------
def verDatos():
    mixto.verDatoMixto()
----------------------------'''
def generarTabla():
    
    for fila in tabla.get_children():
        tabla.delete(fila)
    
    tabla.column("#0", width=100)
    tabla.column("col1", width=100)
    tabla.column("col2", width=100)
    tabla.column("col3", width=100)
    tabla.column("col4", width=100)
    tabla.column("col5", width=100)
    tabla.column("col6", width=100)
    tabla.column("col7", width=100)
    tabla.column("col8", width=100)
    tabla.column("col9", width=100)
    tabla.column("col10", width=100)


    tabla.heading("#0", text="Cantidad Hombres", anchor=CENTER)
    tabla.heading("col1", text="Cantidad Mujeres", anchor=CENTER)
    tabla.heading("col2", text="Fecha creación", anchor=CENTER)
    tabla.heading("col3", text="Tipo", anchor=CENTER)
    tabla.heading("col4", text="Descripción", anchor=CENTER)
    tabla.heading("col5", text="Codigo", anchor=CENTER)
    tabla.heading("col6", text="Nombre", anchor=CENTER)
    tabla.heading("col7", text="Dirección", anchor=CENTER)
    tabla.heading("col8", text="Telefono", anchor=CENTER)
    tabla.heading("col9", text="Director", anchor=CENTER)
    tabla.heading("col10", text="URL", anchor=CENTER)

    for regMixto in listaMixtos:
        tabla.insert("",END, text=regMixto.cant_hombres, values=(regMixto.cant_mujeres))

        for regPublico in listaPublico:
            tabla.insert("",END, text=regPublico.fecha_creacion, values=(regPublico.tipo, regPublico.descripcion))

            for regCentro in listaCentro:
                tabla.insert("",END, text=regCentro.codigo, values=(regCentro.nombre, regCentro.direccion, regCentro.telefono, regCentro.director, regCentro.url))
       
        tabla.pack(fill=tkinter.X)

lbl_title = Label(ventana, text="Tabla General", font=("Arial Black",16 ))

lbl_cant_hombres = Label(ventana, text="Cantidad de hombres", font=("Century",14))
txt_cant_hombres = Entry(ventana, font=("Century",14))

lbl_cant_mujeres = Label(ventana, text="Cantidad de mujeres", font=("Century",14))
txt_cant_mujeres = Entry(ventana, font=("Century",14))

lbl_fecha = Label(ventana, text="Fecha Creación", font=("Century",14))
txt_fecha = Entry(ventana, font=("Century",14))

lbl_tipo = Label(ventana, text="Tipo", font=("Century",14))
txt_tipo = Entry(ventana, font=("Century",14))

lbl_descripcion = Label(ventana, text="Descripcion", font=("Century",14))
txt_descripcion = Entry(ventana, font=("Century",14))

lbl_codigo = Label(ventana, text="Código", font=("Century",14))
txt_codigo = Entry(ventana, font=("Century",14))

lbl_nombre = Label(ventana, text="Nombre", font=("Century",14))
txt_nombre = Entry(ventana, font=("Century",14))

lbl_direccion = Label(ventana, text="Dirección", font=("Century",14))
txt_direccion = Entry(ventana, font=("Century",14))

lbl_telefono = Label(ventana, text="Telefono", font=("Century",14))
txt_telefono = Entry(ventana, font=("Century",14))

lbl_director = Label(ventana, text="Director", font=("Century",14))
txt_director = Entry(ventana, font=("Century",14))

lbl_url = Label(ventana, text="URL", font=("Century",14))
txt_url = Entry(ventana, font=("Century",14))

btn_guardar=Button(ventana, text="Guardar", command=guardarDatos, font=("Arial Black",14))

lbl_title.pack()
lbl_cant_hombres.pack(anchor=tkinter.W)
txt_cant_hombres.pack(fill=tkinter.X)
lbl_cant_mujeres.pack(anchor=tkinter.W)
txt_cant_mujeres.pack(fill=tkinter.X)
lbl_fecha.pack(anchor=tkinter.W)
txt_fecha.pack(fill=tkinter.X)
lbl_tipo.pack(anchor=tkinter.W)
txt_tipo.pack(fill=tkinter.X)
lbl_descripcion.pack(anchor=tkinter.W)
txt_descripcion.pack(fill=tkinter.X)
lbl_codigo.pack(anchor=tkinter.W)
txt_codigo.pack(fill=tkinter.X)
lbl_nombre.pack(anchor=tkinter.W)
txt_nombre.pack(fill=tkinter.X)
lbl_direccion.pack(anchor=tkinter.W)
txt_direccion.pack(fill=tkinter.X)
lbl_telefono.pack(anchor=tkinter.W)
txt_telefono.pack(fill=tkinter.X)
lbl_director.pack(anchor=tkinter.W)
txt_director.pack(fill=tkinter.X)
lbl_url.pack(anchor=tkinter.W)
txt_url.pack(fill=tkinter.X)
btn_guardar.pack(fill=tkinter.X)

ventana.mainloop()