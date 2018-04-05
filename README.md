<b> Proyecto FINAL - Transportes Python v.2.0 </b>
--------------------------------------------------

"Sobre gestón de una empresa de transportes"

El funcionamiento es sencillo, nada mas iniciar ya solo dejará 2 opciones a elegir y no se activará la tercera hasta que se haga lo que indica (busque como hacerlo para activar y desactivar botones)
Contiene una base de datos con 4 tablas que tienen datos metidos y se le añaden mas en los campos de la aplicación correspondientes.
Muestra datos de una fila de esos campos en sus sitios correspondientes
Función para "limpiar" los campos por un botón
Añade datos desde un combobox dependiendo de cual este activo añade a la tabla uno u otro
Una ventana que muestra solo 3 campos de otra tabla por consulta desde el código (ventana furgones)

--------------------------------------------------

<b> RESUMEN CONTENIDO </b>

- 3 Ventanas conectadas entre si
- 1 Base de Datos con 4 Tablas
- Varios botones
- Campos para texto
- ComboBox
- CheckBox (que depende de a cual se le de se desactiva y activan otros)
- Accesos a la base de datos (consulta y añadir)
- Imprime por consola (con print) algunas comprobaciones y/o errores
- Documentación con Pydoc la clase "Informes.py"
- Genera 3 informes con imagen en formato .PDF
- Logo de la "Empresa" creada con GIMP
- Empaquetado

--------------------------------------------------

<b> PARA EMPAQUETADO </b>

  1. Abrir el TERMINAL
  2. Ir a la ruta donde está descargado el proyecto con los archivos "setup.py" y "lanzador"
  3. Ejecutar el comando -- sudo python3 setup.py install --
  4. Una vez instalado escribir -- lanzador -- y se ejutará

<b> NOTA </b>

Si no tenemos python3 instalado ejecutamos el comando:
- -- sudo install python3 -- (en LINUX)
- -- brew install python3 -- (En MAC)

Si tenemos instalado versiones anteriores ejecutamos el comando:
- -- sudo upgrade python -- (en LINUX)
- -- brew upgrade python -- (En MAC)
