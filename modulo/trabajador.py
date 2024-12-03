import mysql.connector
from db.conectar_DB import conectar_db
from modulo.persona import Persona

class Trabajador(Persona):
    """
    Clase para gestionar a los trabajadores del crucero en la base de datos.
    Contiene métodos estáticos para agregar, modificar, listar y borrar trabajadores.
    """

    def __init__(self, nombre, identificacion, id_rol, salario, telefono=None, direccion=None, estado='activo', fecha_ingreso=None):
        super().__init__(nombre, identificacion)
        self.id_rol = id_rol
        self.salario = salario
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        self.fecha_ingreso = fecha_ingreso

    @staticmethod
    def agregar(nombre, identificacion, id_rol, salario, telefono=None, direccion=None, estado='activo', fecha_ingreso=None):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO trabajadores (nombre, identificacion, id_rol, salario, telefono, direccion, estado, fecha_ingreso)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (nombre, identificacion, id_rol, salario, telefono, direccion, estado, fecha_ingreso))
                conn.commit()
                print("Trabajador agregado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al agregar el trabajador: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def modificar(id_trabajador, nombre=None, identificacion=None, id_rol=None, salario=None, telefono=None, direccion=None, estado=None, fecha_ingreso=None):
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
                if id_rol:
                    campos.append("id_rol = %s")
                    valores.append(id_rol)
                if salario:
                    campos.append("salario = %s")
                    valores.append(salario)
                if telefono:
                    campos.append("telefono = %s")
                    valores.append(telefono)
                if direccion:
                    campos.append("direccion = %s")
                    valores.append(direccion)
                if estado:
                    campos.append("estado = %s")
                    valores.append(estado)
                if fecha_ingreso:
                    campos.append("fecha_ingreso = %s")
                    valores.append(fecha_ingreso)

                valores.append(id_trabajador)
                query = f"UPDATE trabajadores SET {', '.join(campos)} WHERE id_trabajador = %s"
                cursor.execute(query, valores)
                conn.commit()
                print(f"Trabajador {id_trabajador} modificado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al modificar el trabajador: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT * FROM trabajadores"
                cursor.execute(query)
                trabajadores = cursor.fetchall()
                if trabajadores:
                    print("\n--- Lista de trabajadores ---")
                    for trabajador in trabajadores:
                        print(f"ID: {trabajador['id_trabajador']} | Nombre: {trabajador['nombre']} | Identificación: {trabajador['identificacion']} | "
                            f"Rol ID: {trabajador['id_rol']} | Salario: {trabajador['salario']} | Teléfono: {trabajador['telefono']} | "
                            f"Dirección: {trabajador['direccion']} | Fecha Ingreso: {trabajador['fecha_ingreso']} |  Estado: {trabajador['estado']} | ")
                else:
                    print("No hay trabajadores registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los trabajadores: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def borrar(id_trabajador):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = "DELETE FROM trabajadores WHERE id_trabajador = %s"
                cursor.execute(query, (id_trabajador,))
                conn.commit()
                print(f"Trabajador {id_trabajador} borrado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al borrar el trabajador: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def obtener_datos_trabajador(id_trabajador):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT * FROM trabajadores WHERE id_trabajador = %s"
                cursor.execute(query, (id_trabajador,))
                trabajador = cursor.fetchone()
                return trabajador
            except mysql.connector.Error as e:
                print(f"Error al obtener datos del trabajador: {e}")
            finally:
                cursor.close()
                conn.close()