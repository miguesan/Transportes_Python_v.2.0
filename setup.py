from distutils.core import setup

setup(name = "TransportesPython",
      version="2.0",
      description="Aplicacion para la empresa de Transportes Python S.L.",
      long_description="""Aplicacion para la gestion,
       envio, y asigancion de paquetes
       con remitente y destinatario
       por base de datos
       y generado de informes""",
      author="Miguel",
      author_email="msanchezblanco@danielcastelao.org",
      url="www.transportespython.es",
      keywords="transportes,envios,furgones,python",
      platforms="Linux,MacOS",
      packages=['paquete'],
      scripts=['lanzador'],
      requires=['reportlab']

      )
