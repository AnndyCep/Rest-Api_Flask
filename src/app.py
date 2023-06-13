# Vamos almacenar el codigo fuente de la aplicación
# Archvo principla para nuestro servidor creado con flaks Cliente servodor

"""
Vamos a utilizar el forato Json Javascript Object Notation, formato de intercambio ligero, para poder
intercambiar datos entre el cliente servidor

"""

from flask import Flask, jsonify , request
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__) 
# Este parametro nos permite saber si estamos ejecutando este archivo como principal
conexion = MySQL(app)
# Se tiene la conexion con la base de datos y trabajar con las tablas que se desee.

@app.route('/cursos', methods=['GET'])
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

@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        # Crearemos la conexion de la base de datos y trabajar con las tab
        cursor = conexion.connection.cursor() # Se crea el cursor necesario para poder trabajar con la base de datos.
        sql = " SELECT * FROM curso WHERE codigo = '{0}'".format(codigo) # se crea la consulta de la base de datos
        cursor.execute(sql) # se ejecuta la consulta, lo que se retornan datos
        datos= cursor.fetchone() #  se alacenan los datos en " datos " y fetchone hace que python los entienda
        if datos != None:
            curso = { 'codigo': datos[0], 'nombre': datos[1] , 'creditos': datos[2] } 
            # creamos un diccionario donde accedemos a los indices de la tupla.
            return jsonify({'curso': curso, 'messages': "Curso encontrado"})
        else:
            return jsonify({'messages':"Curso no encontrado"})
        
    except Exception as ex:
        return jsonify({'messages':"Error"})

@app.route('/cursos', methods=['POST'])
def crear_curso():
    try:
            # Crearemos la conexion de la base de datos y trabajar con las tab
            cursor = conexion.connection.cursor() # Se crea el cursor necesario para poder trabajar con la base de datos.
            sql = " INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')".format(request.json['codigo'],
                                request.json['nombre'], request.json['creditos']) # se crea la consulta de la base de datos
                                # request.json es el objeto de la peticion, encabezados de la peticion  
            cursor.execute(sql) # se ejecuta la consulta, lo que se retornan datos
            conexion.connection.commit() # se confirma la transaccion
            return jsonify({'messages':"Curso creado"})
    
    except Exception as ex:
        return jsonify({'messages':"Error"})

@app.route('/cursos/<codigo>' , methods =["DELETE"])
def eliminar_curso(codigo):
    try:
        # Crearemos la conexion de la base de datos y trabajar con las tab
        cursor = conexion.connection.cursor() # Se crea el cursor necesario para poder trabajar con la base de datos.
        sql = " DELETE FROM curso WHERE codigo = '{0}'".format(codigo) # se crea la consulta de la base de datos
        cursor.execute(sql) # se ejecuta la consulta, lo que se retornan datos
        conexion.connection.commit() # se confirma la transaccion
        return jsonify({'messages':"Curso eliminado"})
    
    except Exception as ex:
        return jsonify({'messages':"Error"})
    
@app.route('/cursos/<codigo>' , methods =["PUT"])
def actualizar_curso(codigo):
    try:
        # Crearemos la conexion de la base de datos y trabajar con las tablas
        cursor = conexion.connection.cursor()
        sql = "UPDATE curso SET nombre = '{0}' ,  creditos = '{1}' WHERE codigo = '{2}'".format(request.json['nombre']
                                                , request.json['creditos'],codigo)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'messages':"Curso actualizado"})
    except Exception as ex:
        return jsonify({'messages' "Error"})

def pagina_no_encontrada(error):
    return "<h1>La pagina no existe............</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development']) # se estaria accediendo a la clase configurationDesarrollo
    app.register_error_handler(404, pagina_no_encontrada) # Permite capturar el error, de la pagina no encontrada.
    app.run()
    # Este codigo nos permite ejecutar el archivo como principal
    # Levantamos el servidor
