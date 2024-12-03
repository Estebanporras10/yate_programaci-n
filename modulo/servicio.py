import mysql.connector
from db.conectar_DB import conectar_db

class Servicio:
    """
    Clase para gestionar los servicios de los pasajeros en el sistema.
    Incluye métodos para registrar, modificar, listar y desactivar servicios.
    """

    @staticmethod
    def registrar(id_cliente, id_trabajador, nombre_servicio, fecha_solicitud, hora_solicitud, costo):
        """
        Registra un nuevo servicio en la base de datos.

        Args:
            id_cliente (int): ID del cliente solicitante.
            id_trabajador (int): ID del trabajador asignado.
            nombre_servicio (str): Nombre del servicio.
            fecha_solicitud (str): Fecha de solicitud en formato 'YYYY-MM-DD'.
            hora_solicitud (str): Hora de solicitud en formato 'HH:MM:SS'.
            costo (float): Costo del servicio.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO servicios 
                    (id_pasajero, id_trabajador, nombre_servicio, fecha_solicitud, hora_solicitud, costo) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (id_cliente, id_trabajador, nombre_servicio, fecha_solicitud, hora_solicitud, costo))
                conn.commit()
                print("Servicio registrado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al registrar el servicio: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def modificar(id_servicio, id_cliente=None, id_trabajador=None, nombre_servicio=None, 
                  fecha_solicitud=None, hora_solicitud=None, costo=None):
        """
        Modifica los detalles de un servicio existente.

        Args:
            id_servicio (int): ID del servicio a modificar.
            id_cliente (int, opcional): Nuevo ID del cliente solicitante.
            id_trabajador (int, opcional): Nuevo ID del trabajador asignado.
            nombre_servicio (str, opcional): Nuevo nombre del servicio.
            fecha_solicitud (str, opcional): Nueva fecha de solicitud.
            hora_solicitud (str, opcional): Nueva hora de solicitud.
            costo (float, opcional): Nuevo costo del servicio.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                campos = []
                valores = []

                if id_cliente:
                    campos.append("id_pasajero = %s")
                    valores.append(id_cliente)
                if id_trabajador:
                    campos.append("id_trabajador = %s")
                    valores.append(id_trabajador)
                if nombre_servicio:
                    campos.append("nombre_servicio = %s")
                    valores.append(nombre_servicio)
                if fecha_solicitud:
                    campos.append("fecha_solicitud = %s")
                    valores.append(fecha_solicitud)
                if hora_solicitud:
                    campos.append("hora_solicitud = %s")
                    valores.append(hora_solicitud)
                if costo is not None:
                    campos.append("costo = %s")
                    valores.append(costo)

                valores.append(id_servicio)
                query = f"UPDATE servicios SET {', '.join(campos)} WHERE id_servicio = %s"
                cursor.execute(query, valores)
                conn.commit()
                print(f"Servicio {id_servicio} modificado con éxito.")
            except mysql.connector.Error as e:
                print(f"Error al modificar el servicio: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        """
        Lista todos los servicios registrados en la base de datos.
        """
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT * FROM servicios"
                cursor.execute(query)
                servicios = cursor.fetchall()
                if servicios:
                    print("\n--- Lista de servicios ---")
                    for servicio in servicios:
                        print(f"ID: {servicio['id_servicio']} | Cliente ID: {servicio['id_pasajero']} | "
                              f"Trabajador ID: {servicio['id_trabajador']} | Servicio: {servicio['nombre_servicio']} | "
                              f"Fecha: {servicio['fecha_solicitud']} | Hora: {servicio['hora_solicitud']} | "
                              f"Costo: {servicio['costo']}")
                else:
                    print("No hay servicios registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los servicios: {e}")
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def listar_servicios():
        conn = conectar_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT 
                        s.id_servicio AS numero_servicio,
                        p.nombre AS nombre_cliente,
                        p.identificacion AS identificacion_cliente,
                        c.numero_cabina,
                        t.nombre AS nombre_funcionario,
                        r.nombre AS rol_funcionario,
                        s.nombre_servicio,
                        s.fecha_solicitud,
                        s.hora_solicitud,
                        s.costo
                    FROM 
                        servicios s
                    JOIN 
                        pasajeros p ON s.id_pasajero = p.id_pasajero
                    JOIN 
                        cabinas c ON p.id_cabina = c.id_cabina
                    JOIN 
                        trabajadores t ON s.id_trabajador = t.id_trabajador
                    JOIN 
                        roles r ON t.id_rol = r.id_rol;
                """
                cursor.execute(query)
                servicios = cursor.fetchall()
                if servicios:
                    print("\n--- Listado General de Servicios ---")
                    for servicio in servicios:
                        print(f"Número de servicio: {servicio['numero_servicio']} | Cliente: {servicio['nombre_cliente']} ({servicio['identificacion_cliente']}) | "
                              f"Cabina: {servicio['numero_cabina']} | Funcionario: {servicio['nombre_funcionario']} | "
                              f"Rol: {servicio['rol_funcionario']} | Servicio: {servicio['nombre_servicio']} | "
                              f"Fecha: {servicio['fecha_solicitud']} | Hora: {servicio['hora_solicitud']} | Monto: {servicio['costo']} |")
                else:
                    print("No hay servicios registrados.")
            except mysql.connector.Error as e:
                print(f"Error al listar los servicios: {e}")
            finally:
                cursor.close()
                conn.close()
