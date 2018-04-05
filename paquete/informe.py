from reportlab.platypus import Table
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import A3
import os
from reportlab.lib import colors
from sqlite3 import connect
from sqlite3 import DatabaseError


guion = []

cabeceiraDestino = [["ID","Nombre Destino","Direccion Destino","Poblacion","Estado","CP","Movil","Telf."]]
cabeceiraRemitente = [["ID","Nombre Remitente","Direccion Remitente","Poblacion","Estado","CP","Telf."]]
cabeceiraFurgon = [["ID","Conductor","Matricula"]]


#acceder os datos da lista con consultas

def generarDestino():
    """
    :return:

    Metodo que genera el informe para los destinos consultando los datos en la base de datos y colocandolos como
    esta indicado en la cabecera
    anhadiendo una imagen al final del informe
    Formato .PDF
    """
    try:
        bbdd = connect("envios.db")
        cursor = bbdd.cursor()
        cursor.execute("SELECT * FROM envios")

        taboa = Table(cabeceiraDestino+cursor.fetchall())


    except DatabaseError as e:
        print("ERROR NA BASE DE DATOS")

    taboa.setStyle([('BOX', (0,0),(-1,-1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

    guion.append(taboa)

#anhade una imagen al pdf
    imaxe = Image(os.path.realpath('transpython.png'))
    guion.append(imaxe)
#creacion del archivo pdf
    doc = SimpleDocTemplate("DatosDestinatarios.pdf", pagesize=A3, showBoundary=1)
    doc.build(guion)
    print("Informe de Destinatarios Xenerado")


def generarRemitente():
    """
    :return:

    Metodo que genera el informe para los remitentes consultando los datos en la base de datos y colocandolos como
    esta indicado en la cabecera
    anhadiendo una imagen al final del informe
    Formato .PDF
    """
    try:
        bbdd = connect("envios.db")
        cursor = bbdd.cursor()
        cursor.execute("SELECT * FROM remitente")

        taboa = Table(cabeceiraRemitente+cursor.fetchall())


    except DatabaseError as e:
        print("ERROR NA BASE DE DATOS")

    taboa.setStyle([('BOX', (0,0),(-1,-1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

    guion.append(taboa)

#anhade una imagen al pdf
    imaxe = Image(os.path.realpath('transpython.png'))
    guion.append(imaxe)
#creacion del archivo pdf
    doc = SimpleDocTemplate("DatosRemitentes.pdf", pagesize=A3, showBoundary=1)
    doc.build(guion)
    print("Informe de Remitentes Xenerado")

def generarFurgon():
    """
    :return:

    Metodo que genera el informe para los furgones consultando los datos en la base de datos y colocandolos como
    esta indicado en la cabecera
    anhadiendo una imagen al final del informe
    Formato .PDF
    """
    try:
        bbdd = connect("envios.db")
        cursor = bbdd.cursor()
        cursor.execute("SELECT * FROM furgon")

        taboa = Table(cabeceiraFurgon+cursor.fetchall())


    except DatabaseError as e:
        print("ERROR NA BASE DE DATOS")

    taboa.setStyle([('BOX', (0,0),(-1,-1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

    guion.append(taboa)

#anhade una imagen al pdf
    imaxe = Image(os.path.realpath('transpython.png'))
    guion.append(imaxe)
#creacion del archivo pdf
    doc = SimpleDocTemplate("DatosFurgones.pdf", pagesize=A4, showBoundary=1)
    doc.build(guion)
    print("Informe de Furgones Xenerado")