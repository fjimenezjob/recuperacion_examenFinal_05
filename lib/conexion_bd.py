''' Class CONEXION, aqui esta la conexion y los metodos para poder conectar a la base de datos '''
import pymysql

CONEXION = pymysql.connect('localhost', 'fran', 'Hello1234', 'cajero')

def insertar_usuario(nombre, apellido_1, apellido_2, dni):
        cursor = CONEXION.cursor()
        cursor.execute(f'''
        INSERT INTO "usuarios" (apellido1, apellido2, dni, nombre)
        VALUES
          (
            "{apellido_1}",
            "{apellido_2}",
            "{dni}",
            "{nombre}"
          )
        ''')
        # Guardar datos
        CONEXION.commit()

def leer_usuario(dni):
        cursor = CONEXION.cursor()
        query = (f'SELECT * FROM usuarios WHERE dni = "{dni}"')
        cursor.execute(query)
        usuario = cursor.fetchall()
        return usuario

def get_dinero(dni):
        cursor = CONEXION.cursor()
        query = (f'SELECT saldo FROM cuentas WHERE dni = "{dni}"')
        cursor.execute(query)
        dinero = cursor.fetchall()
        return dinero[0][0]

def set_dinero(dni, cantidad):
        cursor = CONEXION.cursor()
        cursor.execute(f'''
        UPDATE cuentas SET saldo = {cantidad} WHERE dni = '{dni}'
        ''')
        # Guardar datos
        CONEXION.commit()



def leer_password(dni):
        cursor = CONEXION.cursor()
        cursor.execute(f'''
        SELECT password FROM cuentas WHERE dni = "{dni}"
        ''')
        password = cursor.fetchall()
        return password[0][0]
