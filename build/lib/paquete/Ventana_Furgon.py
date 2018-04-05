import gi

import sqlite3 as dbapi

from paquete import informe

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class ventanaFurgon (Gtk.Window): #crea una ventana

    def cambioVolver (self, boton):
        """
        :param boton:
        :return:

        Método "cambioVolver" que cierra la presente ventana de la interfaz
        """
        self.destroy()

    def botonCargar(self, boton):
        """
        :param boton:
        :return:

        Método "botonCargar" que realiza la consulta en la base de datos
        y coloca los datos obtenidos en sus respectivos lugares asignados para los Gtk.Entry de la interfaz
        """
        try:
            bbdd = dbapi.connect("envios.db")
            print("Comprobando...")

            cursorfurgon = bbdd.cursor()

            cursorfurgon.execute("SELECT * FROM furgon")
            for rexistro in cursorfurgon.fetchmany(2):
                self.txtidFurgon.set_text(rexistro[0])
                self.txtnombreConductor.set_text(rexistro[1])
                self.txtmatricula.set_text(rexistro[2])
            cursorfurgon.close() # cierra el cursor
            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")


    def bInformFurgon(self, boton):
        """
        :param boton:
        :return:

        Método "bInformFurgon" que llama al método de la clase informe que genera uno de los 3 informes
        """
        informe.generarFurgon()

    def __init__(self):
        """
        :return:

        Método que contiene los elementos de la interfaz
        - Labels de informacion Gtk.Label
        - Gtk.Frame
        - Cuadros de texto Gtk.Entry
        - 3 botones que llaman a los métodos explicados anteriormente Gtk.Button
        """
        # crear la ventana principal
        Gtk.Window.__init__(self, title="Furgones de Transportes Python - Nº 6122")
        self.set_border_width(10)
        self.set_default_size(450, 250)

        # crear la caja principal, la base de la ventana
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        # titulo para el programa dentro de la ventana
        lbtitulo = Gtk.Label(xalign=0)  # para la posicion
        lbtitulo.set_markup("<b>Furgones - Transportes Python S.L.</b>")
        cajaPrincipal.add(lbtitulo)

        # PRIMERA PARTE DE LA VENTANA:

        # agregar el frame
        fdatosFurgon = Gtk.Frame(label="Datos del Furgon de Reparto")
        # para agregar una caja vertical 1 dentro del frame para tener posicionado
        cajaInvisibleVert1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        fdatosFurgon.add(cajaInvisibleVert1)
        fdatosFurgon.add(cajaInvisibleHorizontal)

        # añadir contenidos
        lblidFurgon = Gtk.Label("ID Furgon: ", xalign=0)
        cajaInvisibleVert1.add(lblidFurgon)
        self.txtidFurgon = Gtk.Entry()
        cajaInvisibleVert1.add(self.txtidFurgon)

        lblnombreConductor = Gtk.Label("Nombre Conductor: ", xalign=0)
        cajaInvisibleVert1.add(lblnombreConductor)
        self.txtnombreConductor = Gtk.Entry()
        cajaInvisibleVert1.add(self.txtnombreConductor)

        lblmatricula = Gtk.Label("Matricula del Furgon: ", xalign=0)
        cajaInvisibleVert1.add(lblmatricula)
        self.txtmatricula = Gtk.Entry()
        cajaInvisibleVert1.add(self.txtmatricula)

        botonCargar = Gtk.Button("Cargar Datos")
        botonCargar.connect("clicked", self.botonCargar)
        cajaInvisibleVert1.add(botonCargar)

        botonInformeFurgon = Gtk.Button("Generar Informe de Furgones")
        botonInformeFurgon.connect("clicked", self.bInformFurgon)
        cajaInvisibleVert1.add(botonInformeFurgon)

        botonVolver= Gtk.Button("Volver")
        botonVolver.connect("clicked", self.cambioVolver)
        cajaInvisibleVert1.add(botonVolver)


        cajaPrincipal.add(fdatosFurgon)  # agrega la tercera ventana a la principal





        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        # para que se muestre la ventana

if __name__ == "__main__":
        ventana = ventanaFurgon()
        Gtk.main()