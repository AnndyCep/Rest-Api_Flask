# Vamos almacenar el codigo fuente de la aplicación
# Archvo principla para nuestro servidor creado con flaks Cliente servodor

"""
Vamos a utilizar el forato Json Javascript Object Notation, formato de intercambio ligero, para poder
intercambiar datos entre el cliente servidor

"""

from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__) 
# Este parametro nos permite saber si estamos ejecutando este archivo como principal
conexion = MySQL(app)
# Se tiene la conexion con la base de datos y trabajar con las tablas que se desee.

@app.route('/cursos')
def lista_Elememtos():
    try:
        # Crearemos la conexion de la base de datos y trabajar con las tab
        cursor = conexion.connection.cursor() # Se crea el cursor necesario para poder trabajar.
        sql = " SELECT * FROM curso" # se crea la consulta de la base de datos
        cursor.execute(sql) # se ejecuta la consulta, lo que se retornan datos
        datos= cursor.fetchall() #  se alacenan los datos en " datos " y fetchall hace que python los entienda
        cursos = [] # creamos una lista para guardar los datos en formato lista
        for filas in datos: # iteramos la tupla de datos.
            curso = { 'codigo': filas[0], 'nombre': filas[1] , 'creditos': filas[2] } 
            # creamos un diccionario donde accedemos a los indices de la tupla.
            cursos.append(curso) # para luego añadirlos a la lista curso.

        return jsonify({'curso': cursos, 'messages': "Curso listado"})
        # Retornamos los datos en formato Json, con la funcion jsonfy, importamos la libreria
        # enviamos un diccionario con la lista  y un mensaje.s
    except Exception as ex:
        return jsonify({'messages':"Error"})
    
def pagina_no_encontrada(error):
    return "<h1>La pagina no existe............</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development']) # se estaria accediendo a la clase configurationDesarrollo
    app.register_error_handler(404, pagina_no_encontrada) # Permite capturar el error, de la pagina no encontrada.
    app.run()
    # Este codigo nos permite ejecutar el archivo como principal
    # Levantamos el servidor
