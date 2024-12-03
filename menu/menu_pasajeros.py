from modulo.pasajeros import Pasajero
from modulo.cabina import Cabina
from modulo.validaciones import validar_nombre, validar_identificacion, validar_cantidad_personas, validar_fecha, validar_estado

def menu_pasajero():
    """
    Submenú para gestionar los pasajeros. Este menú permite al usuario seleccionar
    una opción para registrar, modificar, listar, desactivar pasajeros o volver al menú principal.
    """
    while True:
        print("\n--- Gestión de Pasajeros ---")
        print("1. Registrar Pasajero")
        print("2. Modificar Pasajero")
        print("3. Listar Pasajeros")
        print("4. Desactivar Pasajero")
        print("5. Listar Pasajeros con cabinas")
        print("6. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            registrar_pasajero_menu()
        elif opcion == "2":
            modificar_pasajero_menu()
        elif opcion == "3":
            Pasajero.listar()
        elif opcion == "4":
            desactivar_pasajero_menu()
        elif opcion == "5":
            Pasajero.listar_con_cabinas()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

def registrar_pasajero_menu():
    """
    Función para registrar un nuevo pasajero.
    Realiza validaciones sobre los datos ingresados antes de registrar el pasajero,
    incluyendo la asignación de una cabina adecuada.
    """
    print("\n--- Registrar Pasajero ---")

    while True:
        nombre = input("Nombre del pasajero: ")
        error = validar_nombre(nombre)
        if error:
            print(error)
        else:
            break

    while True:
        identificacion = input("Identificación del pasajero: ")
        error = validar_identificacion(identificacion)
        if error:
            print(error)
        else:
            break

    while True:
        cantidad_personas = input("Cantidad de personas en la cabina: ")
        error = validar_cantidad_personas(cantidad_personas)
        if error:
            print(error)
        else:
            cantidad_personas = int(cantidad_personas)
            break

    
    cabinas_disponibles = Cabina.listar_disponibles(cantidad_personas)
    if not cabinas_disponibles:
        print(f"No hay cabinas disponibles para {cantidad_personas} personas.")
        return
    
    print("\n--- Lista de cabinas ---")
    for cabina in cabinas_disponibles:
        print(f"ID: {cabina['id_cabina']} | Número: {cabina['numero_cabina']} | "
                            f"Capacidad: {cabina['capacidad']} | Tipo: {cabina['tipo']} | "
                            f"Estado: {cabina['estado']} | Precio por noche: {cabina['precio_noche']} | ")

    
    while True:
        try:
            id_cabina = int(input("Seleccione el ID de la cabina: "))
            if not any(cabina['id_cabina'] == id_cabina for cabina in cabinas_disponibles):
                print("ID de cabina inválido. Por favor, seleccione una de las cabinas disponibles.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de la cabina.")
    
    while True: 
        fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ") 
        error = validar_fecha(fecha_ingreso) 
        if error: 
            print(error) 
        else: 
            break 

    while True: 
        fecha_salida = input("Fecha de salida (YYYY-MM-DD): ") 
        error = validar_fecha(fecha_salida) 
        if error: 
            print(error) 
        else: 
            break

    Pasajero.registrar(nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida)
    Cabina.cambiar_estado(id_cabina, "ocupada")

def modificar_pasajero_menu():
    """
    Función para modificar un pasajero existente. Permite cambiar los valores de los atributos
    con la opción de dejar en blanco los campos que no se deseen modificar.
    """
    print("\n--- Modificar Pasajero ---")
    
    while True:
        try:
            id_pasajero = int(input("ID del pasajero a modificar: "))
            if id_pasajero <= 0:
                print("El ID del pasajero debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID del pasajero.")
    
    print("Deja en blanco los campos que no deseas modificar.")

    while True:
        nombre = input("Nuevo nombre del pasajero: ")
        error = validar_nombre(nombre)
        if error:
            print(error)
        else:
            break

    while True:
        identificacion = input("Nueva identificación del pasajero: ")
        error = validar_identificacion(identificacion)
        if error:
            print(error)
        else:
            break

    while True:
        id_cabina = input("Nueva ID de la cabina asignada: ")
        if id_cabina:
            try:
                id_cabina = int(id_cabina)
                if id_cabina <= 0:
                    print("El ID de la cabina debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el ID de la cabina.")
        else:
            break
    
    while True:
        cantidad_personas = input("Nueva cantidad de personas en la cabina: ")
        error = validar_cantidad_personas(cantidad_personas)
        if error:
            print(error)
        else:
            cantidad_personas = int(cantidad_personas)
            break
    
    while True:  
        fecha_ingreso = input("Nueva fecha de ingreso (YYYY-MM-DD): ")
        error = validar_fecha(fecha_ingreso) 
        if error: 
            print(error) 
        else: 
            break 

    while True: 
        fecha_salida = input("Nueva fecha de salida (YYYY-MM-DD): ")
        error = validar_fecha(fecha_salida) 
        if error: 
            print(error) 
        else: 
            break
    
    while True:   
        estado = input("Nuevo estado del pasajero ('activo' o 'inactivo'): ").lower()
        error = validar_estado(estado) 
        if error: 
            print(error) 
        else: 
            break

    Pasajero.modificar(id_pasajero, nombre, identificacion, id_cabina, cantidad_personas, fecha_ingreso, fecha_salida, estado)

def desactivar_pasajero_menu():
    """
    Función para desactivar un pasajero.
    Solicita el ID del pasajero a desactivar y llama a la función `Pasajero.desactivar()` para actualizar su estado.
    """
    print("\n--- Desactivar Pasajero ---")
    while True:
        try:
            id_pasajero = int(input("ID del pasajero a desactivar: "))
            if id_pasajero <= 0:
                print("El ID debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID del pasajero.")
    
    Pasajero.desactivar(id_pasajero)
