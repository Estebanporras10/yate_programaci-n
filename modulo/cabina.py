import mysql.connector
from db.conectar_DB import conectar_db

class Cabina:
    """
    Clase para gestionar las cabinas en una base de datos.
    Contiene métodos estáticos para registrar, modificar, listar y desactivar cabinas.
    """

    @staticmethod
    def registrar(numero_cabina, capacidad, tipo, precio_noche):
        """
        Registra una nueva cabina en la base de datos.

        Args:
            numero_cabina (str): Número de identificación de la cabina.
            capacidad (int): Capacidad máxima de personas que puede albergar la cabina.
            tipo (str): Tipo de cabina (por ejemplo, 'individual', 'doble').
            precio_noche (float): Precio por noche de la cabina.

        El estado de la cabina se establece como 'disponible' de forma predeterminada.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO cabinas (numero_cabina, capacidad, tipo, precio_noche, estado)
                    VALUES (%s, %s, %s, %s, 'disponible')
                """
                cursor.execute(query, (numero_cabina, capacidad, tipo, precio_noche))
                conn.commit()
                print("Cabina registrada con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al registrar la cabina: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def modificar(id_cabina, numero_cabina=None, capacidad=None, tipo=None, estado=None, precio_noche=None):
        """
        Modifica los detalles de una cabina existente.

        Args:
            id_cabina (int): ID de la cabina a modificar.
            numero_cabina (str, opcional): Nuevo número de la cabina.
            capacidad (int, opcional): Nueva capacidad de la cabina.
            tipo (str, opcional): Nuevo tipo de cabina.
            estado (str, opcional): Nuevo estado de la cabina (por ejemplo, 'disponible', 'mantenimiento').
            precio_noche (float, opcional): Nuevo precio por noche de la cabina.

        Si algún argumento no se proporciona, no se modificará ese campo.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                campos = []  # Lista de campos a modificar
                valores = []  # Lista de los nuevos valores para los campos

                if numero_cabina:
                    campos.append("numero_cabina = %s")
                    valores.append(numero_cabina)
                if capacidad:
                    campos.append("capacidad = %s")
                    valores.append(capacidad)
                if tipo:
                    campos.append("tipo = %s")
                    valores.append(tipo)
                if estado:
                    campos.append("estado = %s")
                    valores.append(estado)
                if precio_noche:
                    campos.append("precio_noche = %s")
                    valores.append(precio_noche)

                valores.append(id_cabina)
                query = f"UPDATE cabinas SET {', '.join(campos)} WHERE id_cabina = %s"
                cursor.execute(query, valores)
                conn.commit()
                print(f"Cabina {id_cabina} modificada con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al modificar la cabina: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        """
        Lista todas las cabinas registradas en la base de datos.

        Muestra la información de todas las cabinas, incluyendo su ID, número, capacidad,
        tipo, estado y precio por noche.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)  # Usar diccionario para acceder a las columnas por nombre
            try:
                query = "SELECT * FROM cabinas"
                cursor.execute(query)
                cabinas = cursor.fetchall()
                if cabinas:
                    print("\n--- Lista de cabinas ---")
                    for cabina in cabinas:
                        print(f"ID: {cabina['id_cabina']} | Número: {cabina['numero_cabina']} | "
                            f"Capacidad: {cabina['capacidad']} | Tipo: {cabina['tipo']} | "
                            f"Estado: {cabina['estado']} | Precio por noche: {cabina['precio_noche']} | ")
                else:
                    print("No hay cabinas registrados.")
                
            except mysql.connector.Error as e:
                print(f"Error al listar las cabinas: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def desactivar(id_cabina):
        """
        Desactiva una cabina, cambiando su estado a 'mantenimiento'.

        Args:
            id_cabina (int): ID de la cabina a desactivar.
        """
        Cabina.modificar(id_cabina, estado="mantenimiento")
        print(f"Cabina {id_cabina} desactivada con éxito.")

    @staticmethod
    def listar_disponibles(cantidad_personas):
        """
        Lista las cabinas disponibles que pueden alojar al menos `cantidad_personas`.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT id_cabina, numero_cabina, capacidad, tipo, estado, precio_noche 
                    FROM cabinas 
                    WHERE capacidad >= %s AND estado = 'disponible'
                """
                cursor.execute(query, (cantidad_personas,))
                cabinas_disponibles = cursor.fetchall()
                return cabinas_disponibles
            except mysql.connector.Error as e:
                print(f"Error al listar las cabinas disponibles: {e}")
                return []
            finally:
                cursor.close()
                conn.close()
        return []
    
    @staticmethod
    def cambiar_estado(id_cabina, nuevo_estado):
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = "UPDATE cabinas SET estado = %s WHERE id_cabina = %s"
                cursor.execute(query, (nuevo_estado, id_cabina))
                conn.commit()
                print(f"Estado de la cabina {id_cabina} cambiado a {nuevo_estado}.")
            except mysql.connector.Error as e:
                print(f"Error al cambiar el estado de la cabina: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar_para(cantidad_personas):
        """
        Lista las cabinas que pueden alojar más de `cantidad_personas`.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT id_cabina, numero_cabina, capacidad, tipo, estado, precio_noche 
                    FROM cabinas 
                    WHERE capacidad = %s
                """
                cursor.execute(query, (cantidad_personas,))
                cabinas = cursor.fetchall()
                if cabinas:
                    print("\n--- Cabinas para más de {} personas ---".format(cantidad_personas))
                    for cabina in cabinas:
                        print(f"ID: {cabina['id_cabina']} | Número: {cabina['numero_cabina']} | "
                              f"Capacidad: {cabina['capacidad']} | Tipo: {cabina['tipo']} | "
                              f"Estado: {cabina['estado']} | Precio por noche: {cabina['precio_noche']} | ")
                else:
                    print(f"No hay cabinas disponibles para más de {cantidad_personas} personas.")
            except mysql.connector.Error as e:
                print(f"Error al listar las cabinas: {e}")
            finally:
                cursor.close()
                conn.close()


