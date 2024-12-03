import re
from modulo.servicio import Servicio
from modulo.pasajeros import Pasajero
from modulo.trabajador import Trabajador
from modulo.validaciones import validar_fecha, validar_estado, validar_salario

def menu_servicio():
    while True:
        print("\n--- Gestión de Servicios ---")
        print("1. Registrar Servicio")
        print("2. Modificar Servicio")
        print("3. Listar tipos de Servicios")
        print("4. Listar servicios por atender")
        print("5. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            registrar_servicio_menu()
        elif opcion == "2":
            modificar_servicio_menu()
        elif opcion == "3":
            Servicio.listar()
        elif opcion == "4":
            Servicio.listar_servicios()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

def registrar_servicio_menu():
    print("\n--- Registrar Servicio ---")

    while True:
        try:
            Pasajero.listar()
            while True:
                id_cliente = input("\nID del cliente solicitante: ")
                if not id_cliente.isdigit():
                    print("El ID del cliente debe ser un número.")
                    continue
                id_cliente = int(id_cliente)
                cliente = Pasajero.obtener_datos_cliente(id_cliente)
                if not cliente:
                    print("Cliente no encontrado. Por favor, intenta de nuevo.")
                else:
                    print(f"\nDatos del Cliente: {cliente}")
                    break

            Trabajador.listar()
            while True:
                id_trabajador = input("ID del trabajador asignado: ")
                if not id_trabajador.isdigit():
                    print("El ID del trabajador debe ser un número.")
                    continue
                id_trabajador = int(id_trabajador)
                trabajador = Trabajador.obtener_datos_trabajador(id_trabajador)
                if not trabajador:
                    print("Trabajador no encontrado. Por favor, intenta de nuevo.")
                else:
                    print(f"Datos del Trabajador: {trabajador['nombre']}")
                    break

            print("\n--- Lista de Tipos de Servicio ---")
            tipos_servicios = ["Servicio de limpieza", "Mantenimiento de cabina", "Servicio de comida", "Spa y masajes", "Excursiones guiadas"]
            for i, servicio in enumerate(tipos_servicios, 1):
                print(f"{i}. {servicio}")
            while True:
                tipo_servicio_opcion = input("Seleccione el tipo de servicio (1-7): ")
                if not tipo_servicio_opcion.isdigit() or int(tipo_servicio_opcion) < 1 or int(tipo_servicio_opcion) > len(tipos_servicios):
                    print("Opción de servicio inválida. Por favor, selecciona un número válido.")
                else:
                    nombre_servicio = tipos_servicios[int(tipo_servicio_opcion) - 1]
                    break

            while True:
                fecha_solicitud = input("Fecha de solicitud (YYYY-MM-DD): ")
                error = validar_fecha(fecha_solicitud)
                if error:
                    print(error)
                else:
                    break

            while True:
                hora_solicitud = input("Hora de solicitud (HH:MM:SS): ")
                if not re.match(r'\d{2}:\d{2}:\d{2}', hora_solicitud):
                    print("Hora inválida. Debe estar en el formato 'HH:MM:SS'.")
                else:
                    break

            while True:
                try:
                    costo = float(input("Costo del servicio: "))
                    if costo <= 0:
                        print("El costo debe ser mayor que 0.")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido para el costo.")

            Servicio.registrar(id_cliente, id_trabajador, nombre_servicio, fecha_solicitud, hora_solicitud, costo)
            break

        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

def modificar_servicio_menu():
    print("\n--- Modificar Servicio ---")
    while True:
        try:
            id_servicio = int(input("ID del servicio a modificar: "))
            if id_servicio <= 0:
                raise ValueError("El ID del servicio debe ser un número entero positivo.")

            Pasajero.listar()
            while True:
                id_cliente = input("Nuevo ID del cliente solicitante: ")
                if not id_cliente.isdigit():
                    print("El ID del cliente debe ser un número.")
                    continue
                id_cliente = int(id_cliente)
                cliente = Pasajero.obtener_datos_cliente(id_cliente)
                if not cliente:
                    print("Cliente no encontrado. Por favor, intenta de nuevo.")
                else:
                    print(f"\nDatos del Cliente: {cliente}")
                    break

            Trabajador.listar()
            while True:
                id_trabajador = input("Nuevo ID del trabajador asignado: ")
                if not id_trabajador.isdigit():
                    print("El ID del trabajador debe ser un número.")
                    continue
                id_trabajador = int(id_trabajador)
                trabajador = Trabajador.obtener_datos_trabajador(id_trabajador)
                if not trabajador:
                    print("Trabajador no encontrado. Por favor, intenta de nuevo.")
                else:
                    print(f"Datos del Trabajador: {trabajador['nombre']}")
                    break

            print("\n--- Lista de Tipos de Servicio ---")
            tipos_servicios = ["Servicio de limpieza", "Mantenimiento de cabina", "Servicio de comida", "Spa y masajes", "Excursiones guiadas"]
            for i, servicio in enumerate(tipos_servicios, 1):
                print(f"{i}. {servicio}")
            while True:
                tipo_servicio_opcion = input("Seleccione el tipo de servicio (1-7): ")
                if not tipo_servicio_opcion.isdigit() or int(tipo_servicio_opcion) < 1 or int(tipo_servicio_opcion) > len(tipos_servicios):
                    print("Opción de servicio inválida. Por favor, selecciona un número válido.")
                else:
                    nombre_servicio = tipos_servicios[int(tipo_servicio_opcion) - 1]
                    break

            while True:
                fecha_solicitud = input("Nueva fecha de solicitud: ")
                error = validar_fecha(fecha_solicitud)
                if error:
                    print(error)
                else:
                    break

            while True:
                hora_solicitud = input("Nueva hora de solicitud: ")
                if not re.match(r'\d{2}:\d{2}:\d{2}', hora_solicitud):
                    print("Hora inválida. Debe estar en el formato 'HH:MM:SS'.")
                else:
                    break

            while True:
                try:
                    costo = float(input("Costo del servicio: "))
                    if costo <= 0:
                        print("El costo debe ser mayor que 0.")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido para el costo.")
            
            Servicio.modificar(
                id_servicio,
                int(id_cliente) if id_cliente else None,
                int(id_trabajador) if id_trabajador else None,
                nombre_servicio if nombre_servicio else None,
                fecha_solicitud if fecha_solicitud else None,
                hora_solicitud if hora_solicitud else None,
                costo if costo else None
            )
            print(f"Servicio {id_servicio} modificado con éxito.")
            break
        
        except ValueError as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
