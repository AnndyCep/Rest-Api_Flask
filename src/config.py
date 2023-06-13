# aqui tendremos los datos aislado en la aplicación

class configuracionDesarrollo():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345'
    MYSQL_DB = 'api_flask'


config = {
    'development' : configuracionDesarrollo
}