import gi

import paquete.Empresa_Transportes

import sqlite3 as dbapi

gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class ventanaPrincipalPrograma (Gtk.Window): #crea una ventana

    def clickear(self, boton):
        """
        :param boton:
        :return:

        Metodo "clickear" que realiza la conexion con la base de datos
        y activa el boton para poder iniciar el programa
        ya que si no se hace con estos pasos no sera posible acceder
        """

        try:
            bbdd = dbapi.connect("envios.db")
            print("Conectado con Exito")
            self.botonInPrograma.set_sensitive(True) #activa el boton
        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def cambioVent(self, boton):

        """
        :param boton:
        :return:

               Metodo "cambioVent" que realiza el cambio a la nueva ventana de la interfaz
               y cierra la actual
        """
        paquete.Empresa_Transportes.ventanaPrograma()
        self.destroy()

    def bSalir(self, boton): #sale del programa y cierra la base de datos

        """
        :param boton:
        :return:

            Metodo "bSalir" que cierra la base de datos y cierra por completo el programa
        """

        try:
            bbdd = dbapi.connect("envios.db")
            print("Cerrando Base de Datos...")
            bbdd.close()
            print("Saliendo del programa...")
            Gtk.main_quit()
            print("Cerrado con Exito")
        except:
            print("Error en el Cierre")

    def __init__(self):
        """
        :return:

            Metodo donde realizamos la colocacion de los elementos en la interfaz

            - Cajas invisibles Gtk.Box
            - Frames Gtk.Frame
            - Labels para la informacion Gtk.Label
            - 3 botones Gtk.Button
            - 1 imagen Gtk.Image
        """
        # crear la ventana principal
        Gtk.Window.__init__(self, title="Iniciando Transportes Python - Nº 6122")
        self.set_border_width(10)
        self.set_default_size(450, 250)

        # crear la caja principal, la base de la ventana
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        # titulo para el programa dentro de la ventana
        lbtitulo = Gtk.Label(xalign=0)  # para la posicion
        lbtitulo.set_markup("<b>Transportes Python S.L.</b>")
        cajaPrincipal.add(lbtitulo)


# PARTE DE LA VENTANA:

        #agregar el frame
        finicioPrograma = Gtk.Frame(label="Iniciar el Servicio de Transportes Python")
        #para agregar una caja vertical 1 dentro del frame para tener posicionado
        cajaInvisibleVert1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        finicioPrograma.add(cajaInvisibleVert1)


        #anhadir contenidos
        lblBlanco1 = Gtk.Label(" ")
        cajaInvisibleVert1.add(lblBlanco1)

        lbliniciarBase = Gtk.Label("Paso 1 - Iniciar la Base de Datos:", xalign=0)
        cajaInvisibleVert1.pack_start(lbliniciarBase, False, False, 0)
        botonInBase = Gtk.Button("INCIAR BASE")
        botonInBase.connect("clicked", self.clickear)
        cajaInvisibleVert1.pack_start(botonInBase, False, False, 0)

        lblBlanco2 = Gtk.Label(" ")
        cajaInvisibleVert1.add(lblBlanco2)

        lblProgramaPrin = Gtk.Label("Paso 2 - Abrir el Programa Principal", xalign=0)
        cajaInvisibleVert1.pack_start(lblProgramaPrin, False, False, 0)
        self.botonInPrograma = Gtk.Button("INICIAR PROGRAMA")
        self.botonInPrograma.set_sensitive(False) #inicia con el boton desactivado
        self.botonInPrograma.connect("clicked", self.cambioVent)
        cajaInvisibleVert1.pack_start(self.botonInPrograma, False, False, 0)

        lblBlanco3 = Gtk.Label(" ")
        cajaInvisibleVert1.add(lblBlanco3)

        lblsalir = Gtk.Label("SALIR DEL PROGRAMA", xalign=0)
        cajaInvisibleVert1.pack_start(lblsalir, False, False, 0)
        botonsalir = Gtk.Button("SALIR")
        botonsalir.connect("clicked", self.bSalir)
        cajaInvisibleVert1.pack_start(botonsalir, False, False, 0)

        lblBlanco4 = Gtk.Label(" ")
        cajaInvisibleVert1.add(lblBlanco4)
        lblBlanco5 = Gtk.Label(" ")
        cajaInvisibleVert1.add(lblBlanco5)

        image = Gtk.Image()
        image.set_from_file('transpython.png')
        cajaInvisibleVert1.add(image)






        cajaPrincipal.add(finicioPrograma)  # agrega la primera parte a la ventana principal


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
                                #para que se muestre la ventana

if __name__ == "__main__":
    ventana = ventanaPrincipalPrograma()
    Gtk.main()