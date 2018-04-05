import gi

import sqlite3 as dbapi

import random
import paquete.informe
import paquete.Ventana_Furgon
#from paquete.Inicio_Programa import ventanaPrincipalPrograma


gi.require_version('Gtk','3.0')

from gi.repository import Gtk


class ventanaPrograma (Gtk.Window): #crea una ventana

    def cambioVentFurgon(self, boton):
        """
        :param boton:
        :return:

        Método "cambioVentFurgon" que realiza el cambio a la nueva ventana de la interfaz
        y sin cerrar la actual
        """
        paquete.Ventana_Furgon.ventanaFurgon()

    def bSalir(self, boton): #sale del programa y cierra la base de datos
        """
        :param boton:
        :return:

            Método "bSalir" que cierra la base de datos y cierra por completo el programa
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

    def comprobarCheck1(self, boton):
        """
        :param boton:
        :return:

        Método "comprobarCheck1" que activa o desactiva la edicion el checkbutton al presionar el contrario añadir o quitar
        """
        self.CheckButton1.set_sensitive(True)
        self.CheckButton2.set_sensitive(False)
        self.txtpagarcontrarrembolso.set_sensitive(False)

    def comprobarCheck2(self, boton):
        """
        :param boton:
        :return:

        Método "comprobarCheck2" que activa o desactiva la edicion el checkbutton al presionar el contrario añadir o quitar
        """
        self.CheckButton1.set_sensitive(False)
        self.CheckButton2.set_sensitive(True)
        self.txtpagarcontrarrembolso.set_sensitive(True)

    def bComprobarEnvios(self,boton):
        """
        :param boton:
        :return:

        Método "bComprobarEnvios" que realiza la consulta en la base de datos
        y coloca los datos obtenidos en sus respectivos lugares asignados para los Gtk.Entry de la interfaz
        """
        try:
            bbdd = dbapi.connect("envios.db")
            print("Comprobando Datos para envio...")

            cursorEnvio = bbdd.cursor()

            cursorEnvio.execute("SELECT * FROM envios")
            for rexistro in cursorEnvio.fetchmany(2):
                self.txtNombreenvio.set_text(rexistro[1])
                self.txtdirecciondestino.set_text(rexistro[2])
                self.txtestado.set_text(rexistro[3])
                self.txtpoblacion.set_text(rexistro[4])
                str(self.txtcp.set_text(rexistro[5]))
                str(self.txttelf.set_text(rexistro[6]))
                str(self.txtmovil.set_text(rexistro[7]))
            cursorEnvio.close()  # cierra el cursor

            cursorRemitente = bbdd.cursor()

            cursorRemitente.execute("SELECT * FROM remitente")
            for rexistro in cursorRemitente.fetchmany(2):
                self.txtNombreremitente.set_text(rexistro[1])
                self.txtdireccionremitente.set_text(rexistro[2])
                self.txtestadoremitente.set_text(rexistro[3])
                self.txtpoblacionremitente.set_text(rexistro[4])
                str(self.txtcpremitente.set_text(rexistro[5]))
                str(self.txttelfremitente.set_text(rexistro[6]))
            cursorRemitente.close()  # cierra el cursor
            bbdd.close()

            cursorEnvio = bbdd.cursor()

            cursorEnvio.execute("SELECT * FROM envios")
            for rexistro in cursorEnvio.fetchmany(2):
                self.txtNombreenvio.set_text(rexistro[1])
                self.txtdirecciondestino.set_text(rexistro[2])
                self.txtestado.set_text(rexistro[3])
                self.txtpoblacion.set_text(rexistro[4])
                str(self.txtcp.set_text(rexistro[5]))
                str(self.txttelf.set_text(rexistro[6]))
                str(self.txtmovil.set_text(rexistro[7]))
            cursorEnvio.close()  # cierra el cursor

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Comprobar los Datos para el envio (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def bAñadirDatosEnvio(self,boton):
        """
        :param boton:
        :return:

        Método "bAñadirDatosEnvio" que añade a la base de datos los datos obtenidos que esten en los Gtk.Entry
        de los respectivos datos
        a su vez que con un random de números comprendidos entre 10 y 50 lo añadirá al ID en la base de datos
        """

        n = random.randint(10,50) #genera un numero aleatorio entre 10 y 50
        id = n

        try:
            bbdd = dbapi.connect("envios.db")
            print("Procesando...")

            cursorAñadirE = bbdd.cursor()
            datosEnvio = (
                id,
                self.txtNombreenvio.get_text(),
                self.txtdirecciondestino.get_text(),
                self.txtestado.get_text(),
                self.txtpoblacion.get_text(),
                str(self.txtcp.get_text()),
                str(self.txttelf.get_text()),
                str(self.txtmovil.get_text())
            )

            cursorAñadirE.execute("INSERT INTO envios VALUES(?,?,?,?,?,?,?,?)", datosEnvio)

            #cursorAñadirE.close()  # cierra el cursor
            #bbdd.commit()  # guarda los cambios

            self.txtNombreenvio.set_text("")
            self.txtdirecciondestino.set_text("")
            self.txtestado.set_text("")
            self.txtpoblacion.set_text("")
            str(self.txtcp.set_text(""))
            str(self.txttelf.set_text(""))
            str(self.txtmovil.set_text(""))

            cursorAñadirR = bbdd.cursor()
            datosRemite = (
            id,
            self.txtNombreremitente.get_text(),
            self.txtdireccionremitente.get_text(),
            self.txtestadoremitente.get_text(),
            self.txtpoblacionremitente.get_text(),
            str(self.txtcpremitente.get_text()),
            str(self.txttelfremitente.get_text())
            )
            cursorAñadirR.execute("INSERT INTO remitente VALUES(?,?,?,?,?,?,?)",datosRemite)

            cursorAñadirE.close()  # cierra el cursor
            cursorAñadirR.close()  # cierra el cursor
            bbdd.commit() #guarda los cambios

            print("Exito al Añadir los datos del Envio")

            print("Vaciando campos del Remitente...")
            self.txtNombreremitente.set_text("")
            self.txtdireccionremitente.set_text("")
            self.txtestadoremitente.set_text("")
            self.txtpoblacionremitente.set_text("")
            str(self.txtcpremitente.set_text(""))
            str(self.txttelfremitente.set_text(""))

            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Añadir los Datos del Remitente (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def bAñadirPago(self, boton):

        """
        :param boton:
        :return:

        Método "bAñadirPago" que añade los datos a la base obtenidos de los datos de un Gtk.ComboBoxText y de un Gtk.Entry
        """

        try:
            bbdd = dbapi.connect("envios.db")
            print("Procesando...")

            cursorAñadirP = bbdd.cursor()
            datosPago = (
                self.comboBox.get_active_text(),
                self.txtpagarcontrarrembolso.get_text()
            )
            cursorAñadirP.execute("INSERT INTO pago VALUES(?,?)", datosPago)

            cursorAñadirP.close()  # cierra el cursor
            bbdd.commit()  # guarda los cambios

            print("Exito al Añadir Pago")

            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Añadir los Datos del Pago (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def bInformDestino(self, boton):
        """
        :param boton:
        :return:

        Método "bInformDestino" que llama al método de la clase informe que genera uno de los 3 informes
        """
        paquete.informe.generarDestino()

    def bInformRemitente(self, boton):
        """
        :param boton:
        :return:

        Método "bInformRemitente" que llama al método de la clase informe que genera uno de los 3 informes
        """
        paquete.informe.generarRemitente()

    def __init__(self):
        """
        :return:

        Método donde realizamos la colocacion de los elementos en la interfaz

            - Cajas invisibles Gtk.Box
            - Frames Gtk.Frame
            - Labels para la informacion Gtk.Label
            - Cuadros de texto para los datos Gtk.Entry
            - Botones que llaman a los metodos explicados anteriormente Gtk.Button
            - 1 Gtk.ComboBoxText
            - 2 Gtk.CheckButton
        """
        #crear la ventana principal
        Gtk.Window.__init__(self, title="Transportes Python - Nº 6122")
        self.set_border_width(10)
        self.set_default_size(450, 250)

        #crear la caja principal, la base de la ventana
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        #titulo para el programa dentro de la ventana
        lbtitulo = Gtk.Label(xalign=0) #para la posicion
        lbtitulo.set_markup("<b>Transportes Python S.L.</b>")
        cajaPrincipal.add(lbtitulo)

        grid1 = Gtk.Grid()
        self.add(grid1)

        self.cajaH1 = cajaInvisibleHor1 = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.cajaH1)

#PRIMERA PARTE DE LA VENTANA:

        #agregar el frame
        fdatos = Gtk.Frame(label="Datos del Envio")
        #para agregar una caja vertical 1 dentro del frame para tener posicionado


        cajaInvisibleFramePrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # para el destinatario
        cajaInvisibleLabelBlanco1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleLabelBlanco11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleLabelDes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleFrame1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelBlanco1)
        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelBlanco11)

        fdatos.add(cajaInvisibleFramePrincipal)

        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelDes)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame1)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame2)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame3)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame4)
        cajaInvisibleFrameBotones1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrameBotones1)

        #para el remitente
        cajaInvisibleLabelBlanco2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleLabelBlanco22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleLabelRem = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleFrame5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFrame8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleLabelBlancoBotones = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelBlanco2)
        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelBlanco22)


        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelRem)

        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame5)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame6)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame7)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrame8)
        cajaInvisibleFrameBotones2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleFramePrincipal.add(cajaInvisibleLabelBlancoBotones)
        cajaInvisibleFramePrincipal.add(cajaInvisibleFrameBotones2)


        #añadir contenidos
        lblBlanco1 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlanco1.add(lblBlanco1)

        lbldDestinatario = Gtk.Label("DATOS DESTINATARIO        ", xalign=0)
        cajaInvisibleLabelDes.add(lbldDestinatario)

        lblBlanco11 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlanco11.add(lblBlanco11)

        lblNombreenvio = Gtk.Label("Nombre Destinatario ", xalign=0)
        #cajaInvisibleVert1.add(lblNombreenvio)
        cajaInvisibleFrame1.pack_start(lblNombreenvio, False, False, 0)
        self.txtNombreenvio = Gtk.Entry()
        #cajaInvisibleVert1.add(self.txtNombreenvio)
        cajaInvisibleFrame1.pack_start(self.txtNombreenvio, True, True, 0)

        lbldirecciondestino = Gtk.Label("Dirección Destino ", xalign=0)
        cajaInvisibleFrame1.pack_start(lbldirecciondestino, False, False, 10)
        self.txtdirecciondestino = Gtk.Entry()
        cajaInvisibleFrame1.pack_start(self.txtdirecciondestino, True, True, 0)


        # para agregar una caja horizontal dentro del frame para tener posicionado

        lblestado = Gtk.Label("Estado Destinatario ")
        cajaInvisibleFrame2.pack_start(lblestado, False, True, 0)
        self.txtestado = Gtk.Entry()
        cajaInvisibleFrame2.pack_start(self.txtestado, True, True, 0)

        lblpoblacion = Gtk.Label("Población Destinatario ")
        cajaInvisibleFrame2.pack_start(lblpoblacion, False, True, 10)
        self.txtpoblacion = Gtk.Entry()
        cajaInvisibleFrame2.pack_start(self.txtpoblacion, True, True, 0)

        lblcp = Gtk.Label("C.P. Destinatario ",xalign=0)
        self.txtcp = Gtk.Entry()
        cajaInvisibleFrame3.pack_end(self.txtcp, False, True, 0)
        cajaInvisibleFrame3.pack_end(lblcp, False, True, 0)

        lbltelf = Gtk.Label("Telf. Destinatario ", xalign=0)
        cajaInvisibleFrame4.pack_start(lbltelf, False, False, 0)
        self.txttelf = Gtk.Entry()
        cajaInvisibleFrame4.pack_start(self.txttelf, False, False, 0)

        lblmovil = Gtk.Label("Movil Destinatario ", xalign=0)
        cajaInvisibleFrame4.pack_start(lblmovil, False, False, 10)
        self.txtmovil = Gtk.Entry()
        cajaInvisibleFrame4.pack_start(self.txtmovil, False, False, 0)


#SEGUNDA PARTE DE LA VENTANA:

        # añadir contenidos

        lblBlanco2 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlanco2.add(lblBlanco2)

        lbldRemitente= Gtk.Label("DATOS REMITENTE        ", xalign=0)
        cajaInvisibleLabelRem.add(lbldRemitente)

        lblBlanco22 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlanco22.add(lblBlanco22)

        lblNombreremitente= Gtk.Label("Nombre/Empresa Remitente ", xalign=0)
        cajaInvisibleFrame5.pack_start(lblNombreremitente, False, False, 0)
        self.txtNombreremitente = Gtk.Entry()
        cajaInvisibleFrame5.pack_start(self.txtNombreremitente, False, False, 0)

        lbldireccionremitente = Gtk.Label("Dirección Remitente ", xalign=0)
        cajaInvisibleFrame5.pack_start(lbldireccionremitente, False, False, 10)
        self.txtdireccionremitente = Gtk.Entry()
        cajaInvisibleFrame5.pack_start(self.txtdireccionremitente, True, True, 0)


        lblestadoremitente = Gtk.Label("Estado Remitente", xalign=0)
        cajaInvisibleFrame6.pack_start(lblestadoremitente, False, True, 0)
        self.txtestadoremitente = Gtk.Entry()
        cajaInvisibleFrame6.pack_start(self.txtestadoremitente, True, True, 0)

        lblpoblacionremitente = Gtk.Label("Población Remitente", xalign=0)
        cajaInvisibleFrame6.pack_start(lblpoblacionremitente, False, True, 10)
        self.txtpoblacionremitente = Gtk.Entry()
        cajaInvisibleFrame6.pack_start(self.txtpoblacionremitente, True, True, 0)

        lblcpremitente = Gtk.Label("C.P. Remitente", xalign=0)
        self.txtcpremitente = Gtk.Entry()
        cajaInvisibleFrame7.pack_end(self.txtcpremitente, False, True, 0)
        cajaInvisibleFrame7.pack_end(lblcpremitente, False, True, 0)

        lbltelfremitente = Gtk.Label("Telf. Remitente", xalign=0)
        cajaInvisibleFrame8.pack_start(lbltelfremitente, False, False, 0)
        self.txttelfremitente = Gtk.Entry()
        cajaInvisibleFrame8.pack_start(self.txttelfremitente, False, False, 0)

        lblBlancoBotones = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlancoBotones.add(lblBlancoBotones)

        bComprobarEnvios = Gtk.Button("Comprobar Datos")
        bComprobarEnvios.connect("clicked", self.bComprobarEnvios)
        cajaInvisibleFrameBotones2.pack_start(bComprobarEnvios, True, False, 0)

        bAñadirDatosEnvio = Gtk.Button("Añadir Datos del Envio a la Base")
        bAñadirDatosEnvio.connect("clicked", self.bAñadirDatosEnvio)
        cajaInvisibleFrameBotones2.pack_end(bAñadirDatosEnvio, True, False, 0)

# TERCERA PARTE DE LA VENTANA:

        # agregar el frame
        fenvio = Gtk.Frame(label="Envio")
        # para agregar una caja vertical dentro del frame para tener posicionado

        cajaInvisibleVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleHorizontal7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleLabelBlancoEnvio1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleLabelBlancoEnvio2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleLabelBlancoEnvio3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        fenvio.add(cajaInvisibleVertical)
        cajaInvisibleVertical.add(cajaInvisibleHorizontal7)

        cajaInvisibleVertical.add(cajaInvisibleLabelBlancoEnvio1)

        cajaInvisibleVertical.add(cajaInvisibleHorizontal8)

        cajaInvisibleVertical.add(cajaInvisibleLabelBlancoEnvio2)

        cajaInvisibleVertical.add(cajaInvisibleHorizontal9)
        cajaInvisibleVertical.add(cajaInvisibleHorizontal10)

        cajaInvisibleVertical.add(cajaInvisibleLabelBlancoEnvio3)

        cajaInvisibleVertical.add(cajaInvisibleHorizontal11)


        #añadir el comboBox
        lbltipoenvio = Gtk.Label("Tipo de Envio",xalign=0)
        cajaInvisibleHorizontal7.add(lbltipoenvio)
        self.comboBox = Gtk.ComboBoxText()
        self.comboBox.insert(0,"0","24h")
        self.comboBox.insert(1, "1", "48h")
        self.comboBox.insert(2, "2", "72h")
        cajaInvisibleHorizontal7.add(self.comboBox)

        lblBlancoEnvio1 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlancoEnvio1.add(lblBlancoEnvio1)

        lblcontrareembolso = Gtk.Label("¿Contrareembolso?",xalign=0)
        cajaInvisibleHorizontal8.pack_start(lblcontrareembolso, False, False, 10)

        lblBlancoEnvio2 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlancoEnvio2.add(lblBlancoEnvio2)

                # añadir los checkbutton
        self.CheckButton1 = Gtk.CheckButton("Ninguno")
        self.CheckButton1.connect("clicked", self.comprobarCheck1)
        cajaInvisibleHorizontal9.pack_start(self.CheckButton1, False, False, 0)

        self.CheckButton2 = Gtk.CheckButton("Si, a pagar ")
        self.CheckButton2.connect("clicked", self.comprobarCheck2)
        cajaInvisibleHorizontal10.pack_start(self.CheckButton2, False, False, 0)

        self.txtpagarcontrarrembolso = Gtk.Entry()
        self.txtpagarcontrarrembolso.set_sensitive(False)
        cajaInvisibleHorizontal10.pack_start(self.txtpagarcontrarrembolso, False, False, 0)

        lblBlancoEnvio3 = Gtk.Label(" ", xalign=0)
        cajaInvisibleLabelBlancoEnvio3.add(lblBlancoEnvio3)

        self.bPago = Gtk.Button("Añadir Datos")
        self.bPago.connect("clicked", self.bAñadirPago)
        cajaInvisibleHorizontal11.pack_start(self.bPago, False, False, 0)

        botonVerFurgon= Gtk.Button("Ver Furgones Asignados")
        botonVerFurgon.connect("clicked", self.cambioVentFurgon)
        cajaInvisibleHorizontal11.pack_end(botonVerFurgon, False, False, 0)

        #Informes

        finformes = Gtk.Frame(label="Informes")

        cajaInvisibleHorizontal12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        finformes.add(cajaInvisibleHorizontal12)

        botonInformeDestino = Gtk.Button("GENERAR INFORME DESTINOS")
        botonInformeDestino.connect("clicked", self.bInformDestino)
        cajaInvisibleHorizontal12.pack_end(botonInformeDestino, False, False, 0)

        botonInformeRemitente = Gtk.Button("GENERAR INFORME REMITENTES")
        botonInformeRemitente.connect("clicked", self.bInformRemitente)
        cajaInvisibleHorizontal12.pack_start(botonInformeRemitente, False, False, 0)

        #Boton Salir

        fsalir = Gtk.Frame()

        cajaInvisibleHorizontal13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        fsalir.add(cajaInvisibleHorizontal13)

        botonsalir = Gtk.Button("SALIR")
        botonsalir.connect("clicked", self.bSalir)
        cajaInvisibleHorizontal13.pack_end(botonsalir, False, False, 0)

        cajaPrincipal.add(fdatos)#agrega la primera parte a la ventana principal
        cajaPrincipal.add(fenvio)  # agrega la tercera ventana a la principal
        cajaPrincipal.add(finformes)# agrega la cuarta ventana a la principal
        cajaPrincipal.add(fsalir)# agrega la quinta ventana a la principal










        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
                                #para que se muestre la ventana
if __name__ == "__main__":
    ventana = paquete.ventanaPrincipalPrograma()
    Gtk.main()