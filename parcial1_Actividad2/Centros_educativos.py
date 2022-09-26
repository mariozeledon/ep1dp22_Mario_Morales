from tkinter import commondialog


class Centro():
    codigo=0
    nombre=""
    direccion=""
    telefono=0
    director=""
    url=""

    def verDatoCentro(self):
        print("Codigo: ", self.codigo,"Nombre: ",self.nombre,"Dirección: ",self.direccion,"Telefono: ",self.telefono,"Director: ",self.director,"URL: ",self.url)