from modulo.trabajador import Trabajador
from modulo.roles import Roles
import re
from modulo.validaciones import validar_nombre, validar_identificacion, validar_fecha, validar_estado, validar_id_rol, validar_salario, validar_direccion, validar_telefono

def menu_trabajadores():
    """
    Función que muestra el menú principal para gestionar los trabajadores.
    
    El menú ofrece las siguientes opciones:
    - Agregar trabajador
    - Modificar trabajador
    - Listar trabajadores
    - Borrar trabajador
    - Salir
    
    El menú se ejecuta en un ciclo infinito hasta que el usuario seleccione la opción de salir.
    """
    while True:
        print("\n--- Gestión de Trabajadores ---")
        print("1. Agregar Trabajador")
        print("2. Modificar Trabajador")
        print("3. Listar Trabajadores")
        print("4. Borrar Trabajador")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_trabajador_menu()
        elif opcion == "2":
            modificar_trabajador_menu()
        elif opcion == "3":
            Trabajador.listar()
        elif opcion == "4":
            borrar_trabajador_menu()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

def agregar_trabajador_menu():
    """
    Función que muestra el menú para agregar un nuevo trabajador a la base de datos.
    """
    print("\n--- Agregar Trabajador ---")
    
    while True:
        nombre = input("Nombre del Trabajador: ")
        error = validar_nombre(nombre)
        if error:
            print(error)
        else:
            break

    while True:
        identificacion = input("Identificación del Trabajador: ")
        error = validar_identificacion(identificacion)
        if error:
            print(error)
        else:
            break
    
    print("\n--- ID Roles ---")
    Roles.listar()

    while True:
        id_rol = input("ID del rol del trabajador: ")
        error = validar_id_rol(id_rol)
        if error:
            print(error)
        else:
            id_rol = int(id_rol)
            break
    
    while True:
        salario = input("Salario del trabajador: ")
        error = validar_salario(salario)
        if error:
            print(error)
        else:
            salario = float(salario)
            break
    
    while True:
        estado = input("Estado (activo/inactivo): ").lower()
        error = validar_estado(estado)
        if error:
            print(error)
        else:
            break
    
    while True:
        telefono = input("Teléfono del trabajador: ")
        error = validar_telefono(telefono)
        if error:
            print(error)
        else:
            break

    while True:
        direccion = input("Dirección del trabajador: ")
        error = validar_direccion(direccion)
        if error:
            print(error)
        else:
            break

    while True:
        fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ")
        error = validar_fecha(fecha_ingreso)
        if error:
            print(error)
        else:
            break
    
    Trabajador.agregar(nombre, identificacion, id_rol, salario, telefono, direccion, estado, fecha_ingreso)

def modificar_trabajador_menu():
    """
    Función que muestra el menú para modificar un trabajador existente en la base de datos.
    """
    print("\n--- Modificar Trabajador ---")
    
    while True:
        try:
            id_trabajador = int(input("ID del trabajador a modificar: "))
            if id_trabajador <= 0:
                print("El ID debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de trabajador.")
    
    nombre = input("Nuevo nombre del trabajador (deja en blanco para no modificar): ") or None
    identificacion = input("Nueva identificación (deja en blanco para no modificar): ") or None
    
    while True:
        try:
            id_rol = input("Nuevo ID de rol (deja en blanco para no modificar): ")
            if id_rol:
                id_rol = int(id_rol)
                if id_rol <= 0:
                    print("El ID de rol debe ser un número entero positivo.")
                else:
                    break
            else:
                id_rol = None
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de rol.")
    
    salario = input("Nuevo salario (deja en blanco para no modificar): ")
    salario = float(salario) if salario else None
    
    estado = input("Nuevo estado (activo/inactivo) o presiona Enter para no modificar: ").lower() or None
    
    telefono = input("Nuevo teléfono (deja en blanco para no modificar): ") or None
    direccion = input("Nueva dirección (deja en blanco para no modificar): ") or None
    
    fecha_ingreso = input("Nueva fecha de ingreso (YYYY-MM-DD) o presiona Enter para no modificar: ")
    if fecha_ingreso:
        try:
            from datetime import datetime
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        except ValueError:
            print("Fecha inválida. El formato debe ser 'YYYY-MM-DD'.")
            fecha_ingreso = None
    
    Trabajador.modificar(id_trabajador, nombre, identificacion, id_rol, salario, telefono, direccion, estado, fecha_ingreso)


def borrar_trabajador_menu():
    """
    Función que muestra el menú para borrar un trabajador de la base de datos.
    """
    print("\n--- Borrar Trabajador ---")
    while True:
        try:
            id_trabajador = int(input("ID del trabajador a borrar: "))
            if id_trabajador <= 0:
                print("El ID debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de trabajador.")
    
    Trabajador.borrar(id_trabajador)
