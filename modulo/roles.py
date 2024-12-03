import mysql.connector
from db.conectar_DB import conectar_db

class Roles:
    """
    Clase para gestionar los roles en una base de datos.
    Contiene métodos estáticos para agregar, modificar, listar y borrar roles.
    """

    @staticmethod
    def agregar(nombre, descripcion, nivel_acceso, estado):
        """
        Agrega un nuevo rol a la base de datos.

        Args:
            nombre (str): Nombre del rol.
            descripcion (str): Descripción del rol.
            nivel_acceso (int): Nivel de acceso asociado al rol.
            estado (str): Estado del rol (por ejemplo, 'activo' o 'inactivo').

        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO roles (nombre, descripcion, nivel_acceso, estado)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (nombre, descripcion, nivel_acceso, estado))
                conn.commit()
                print("Rol agregado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al agregar el rol: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def modificar(id_rol, nombre=None, descripcion=None, nivel_acceso=None, estado=None):
        """
        Modifica un rol existente en la base de datos.

        Args:
            id_rol (int): ID del rol a modificar.
            nombre (str, opcional): Nuevo nombre del rol.
            descripcion (str, opcional): Nueva descripción del rol.
            nivel_acceso (int, opcional): Nuevo nivel de acceso del rol.
            estado (str, opcional): Nuevo estado del rol (por ejemplo, 'activo' o 'inactivo').

        Si algún argumento no se proporciona, no se modificará ese campo.

        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                campos = []  # Lista de los campos a modificar
                valores = []  # Lista de los nuevos valores para los campos

                if nombre:
                    campos.append("nombre = %s")
                    valores.append(nombre)
                if descripcion:
                    campos.append("descripcion = %s")
                    valores.append(descripcion)
                if nivel_acceso:
                    campos.append("nivel_acceso = %s")
                    valores.append(nivel_acceso)
                if estado:
                    campos.append("estado = %s")
                    valores.append(estado)

                valores.append(id_rol)
                query = f"UPDATE roles SET {', '.join(campos)} WHERE id_rol = %s"
                cursor.execute(query, valores)
                conn.commit()
                print(f"Rol {id_rol} modificado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al modificar el rol: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        """
        Lista todos los roles registrados en la base de datos.

        Muestra la información de todos los roles, incluyendo su ID, nombre, descripción,
        nivel de acceso y estado.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = "SELECT * FROM roles"
                cursor.execute(query)
                roles = cursor.fetchall()
                if roles:
                    print("\n--- Lista de Roles ---")
                    for rol in roles:
                        print(f"ID: {rol[0]} | Nombre: {rol[1]} | Descripción: {rol[2]} | Nivel de acceso: {rol[3]} | Estado: {rol[5]} | ")
                else:
                    print("No hay roles registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los roles: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def borrar(id_rol):
        """
        Elimina un rol de la base de datos.

        Args:
            id_rol (int): ID del rol a eliminar.

        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = "DELETE FROM roles WHERE id_rol = %s"
                cursor.execute(query, (id_rol,))
                conn.commit()
                print(f"Rol {id_rol} borrado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al borrar el rol: {e}")
            finally:
                cursor.close()
                conn.close()
