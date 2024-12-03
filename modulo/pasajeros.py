import mysql.connector
from modulo.persona import Persona
from db.conectar_DB import conectar_db

class Pasajero(Persona):
    """
    Clase para gestionar los pasajeros en un crucero.
    Incluye métodos para registrar, modificar, listar y desactivar pasajeros.
    """

    def __init__(self, nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida):
        super().__init__(nombre, identificacion)
        self.id_cabina = id_cabina
        self.cantidad_personas = cantidad_personas
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida

    @staticmethod
    def registrar(nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO pasajeros 
                    (nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida, estado) 
                    VALUES (%s, %s, %s, %s, %s, %s, 'activo')
                """
                cursor.execute(query, (nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida))
                conn.commit()
                print("Pasajero registrado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al registrar el pasajero: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def modificar(id_pasajero, nombre=None, identificacion=None, id_cabina=None, cantidad_personas=None, 
                  fecha_ingreso=None, fecha_salida=None, estado=None):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                campos = []
                valores = []

                if nombre:
                    campos.append("nombre = %s")
                    valores.append(nombre)
                if identificacion:
                    campos.append("identificacion = %s")
                    valores.append(identificacion)
                if id_cabina:
                    campos.append("id_cabina = %s")
                    valores.append(id_cabina)
                if cantidad_personas:
                    campos.append("cantidad_personas = %s")
                    valores.append(cantidad_personas)
                if fecha_ingreso:
                    campos.append("fecha_ingreso = %s")
                    valores.append(fecha_ingreso)
                if fecha_salida:
                    campos.append("fecha_salida = %s")
                    valores.append(fecha_salida)
                if estado:
                    campos.append("estado = %s")
                    valores.append(estado)

                valores.append(id_pasajero)
                query = f"UPDATE pasajeros SET {', '.join(campos)} WHERE id_pasajero = %s"
                cursor.execute(query, valores)
                conn.commit()
                print(f"Pasajero {id_pasajero} modificado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al modificar el pasajero: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT * FROM pasajeros"
                cursor.execute(query)
                pasajeros = cursor.fetchall()
                if pasajeros:
                    print("\n--- Lista de pasajeros ---")
                    for pasajero in pasajeros:
                        print(f"ID: {pasajero['id_pasajero']} | Nombre: {pasajero['nombre']} | "
                              f"Identificación: {pasajero['identificacion']} | Cabina: {pasajero['id_cabina']} | "
                              f"Personas: {pasajero['cantidad_personas']} | Ingreso: {pasajero['fecha_ingreso']} | "
                              f"Salida: {pasajero['fecha_salida']} | Estado: {pasajero['estado']} | ")
                else:
                    print("No hay pasajeros registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los pasajeros: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def desactivar(id_pasajero):
        Pasajero.modificar(id_pasajero, estado="inactivo")
        print(f"Pasajero {id_pasajero} desactivado con éxito.")

    @staticmethod
    def obtener_datos_cliente(id_cliente):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT * FROM pasajeros WHERE id_pasajero = %s"
                cursor.execute(query, (id_cliente,))
                cliente = cursor.fetchone()
                return cliente
            except mysql.connector.Error as e:
                print(f"Error al obtener datos del cliente: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar_con_cabinas():
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT p.id_pasajero, p.nombre, p.identificacion, c.numero_cabina
                    FROM pasajeros p
                    JOIN cabinas c ON p.id_cabina = c.id_cabina;
                """
                cursor.execute(query)
                pasajeros_con_cabinas = cursor.fetchall()
                if pasajeros_con_cabinas:
                    print("\n--- Lista de Pasajeros y sus Cabinas ---")
                    for pasajero in pasajeros_con_cabinas:
                        print(f"ID: {pasajero['id_pasajero']} | Nombre: {pasajero['nombre']} | "
                              f"Identificación: {pasajero['identificacion']} | Cabina: {pasajero['numero_cabina']} | ")
                else:
                    print("No hay pasajeros registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los pasajeros y sus cabinas: {e}")
            finally:
                cursor.close()
                conn.close()
