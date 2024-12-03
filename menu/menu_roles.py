from modulo.roles import Roles

def menu_roles():
    """
    Función que muestra el menú principal para gestionar los roles.
    
    El menú ofrece las siguientes opciones:
    - Agregar rol
    - Modificar rol
    - Listar roles
    - Borrar rol
    - Salir
    
    El menú se ejecuta en un ciclo infinito hasta que el usuario seleccione la opción de salir.
    """
    while True:
        print("\n--- Gestión de Roles ---")
        print("1. Agregar Rol")
        print("2. Modificar Rol")
        print("3. Listar Roles")
        print("4. Borrar Rol")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_rol_menu()
        elif opcion == "2":
            modificar_rol_menu()
        elif opcion == "3":
            Roles.listar()
        elif opcion == "4":
            borrar_rol_menu()
        elif opcion == "5":
            break 
        else:
            print("Opción no válida. Por favor intente nuevamente.")

def agregar_rol_menu():
    """
    Función que muestra el menú para agregar un nuevo rol a la base de datos.
    
    Esta función solicita al usuario ingresar el nombre del rol, el nivel de acceso, 
    una descripción y el estado (activo o inactivo). Realiza validaciones para asegurar
    que los datos ingresados sean correctos antes de llamar a la función para agregar 
    el rol en la base de datos.

    Se realizan las siguientes validaciones:
    - El nombre del rol no debe contener números ni superar los 50 caracteres.
    - El nivel de acceso debe ser un número entre 1 y 5.
    - El estado debe ser 'activo' o 'inactivo'.
    """
    print("\n--- Agregar Rol ---")
    
    while True:
        nombre = input("Nombre del rol: ")
        if len(nombre) > 50:
            print("El nombre no puede exceder 100 caracteres.")
        elif any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números.")
        else:
            break
    
    while True:
        try:
            nivel_acceso = int(input("Nivel de acceso (1-5): "))
            if nivel_acceso < 1 or nivel_acceso > 5:
                print("El nivel de acceso debe ser entre 1 y 5.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el nivel de acceso.")
    
    descripcion = input("Descripción del rol: ")
    
    while True:
        estado = input("Estado (activo/inactivo): ").lower()
        if estado not in ['activo', 'inactivo']:
            print("Estado inválido. Debe ser 'activo' o 'inactivo'.")
        else:
            break
    
    Roles.agregar(nombre, descripcion, nivel_acceso, estado)

def modificar_rol_menu():
    """
    Función que muestra el menú para modificar un rol existente en la base de datos.
    
    Esta función solicita al usuario el ID del rol que desea modificar y los nuevos datos 
    (nombre, descripción, nivel de acceso y estado). Si algún campo no se quiere modificar, 
    se puede dejar en blanco. Realiza las validaciones para asegurarse de que los datos 
    sean correctos antes de llamar a la función para modificar el rol en la base de datos.

    Se realizan las siguientes validaciones:
    - El ID del rol debe ser un número entero positivo.
    - El nivel de acceso debe ser un número entre 1 y 5.
    - El estado debe ser 'activo' o 'inactivo'.

    Ejemplo de uso:
    >>> modificar_rol_menu()
    """
    print("\n--- Modificar Rol ---")
    
    while True:
        try:
            id_rol = int(input("ID del rol a modificar: "))
            if id_rol <= 0:
                print("El ID debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de rol.")
    
    nombre = input("Nuevo nombre del rol (deja en blanco para no modificar): ") or None
    descripcion = input("Nueva descripción (deja en blanco para no modificar): ") or None
    
    while True:
        try:
            nivel_acceso = input("Nuevo nivel de acceso (1-5) o presiona Enter para no modificar: ")
            if nivel_acceso:
                nivel_acceso = int(nivel_acceso)
                if nivel_acceso < 1 or nivel_acceso > 5:
                    print("El nivel de acceso debe ser entre 1 y 5.")
                else:
                    break
            else:
                nivel_acceso = None
                break
        except ValueError:
            print("Por favor ingrese un número válido para el nivel de acceso.")
    
    estado = input("Nuevo estado (activo/inactivo) o presiona Enter para no modificar: ").lower() or None

    Roles.modificar(id_rol, nombre, descripcion, nivel_acceso, estado)

def borrar_rol_menu():
    """
    Función que muestra el menú para borrar un rol de la base de datos.
    
    Esta función solicita al usuario el ID del rol que desea borrar. Realiza las validaciones
    necesarias para asegurarse de que el ID sea un número entero positivo antes de llamar 
    a la función para borrar el rol de la base de datos.

    Se realiza la siguiente validación:
    - El ID del rol debe ser un número entero positivo.

    Ejemplo de uso:
    >>> borrar_rol_menu()
    """
    print("\n--- Borrar Rol ---")
    while True:
        try:
            id_rol = int(input("ID del rol a borrar: "))
            if id_rol <= 0:
                print("El ID debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de rol.")
    
    Roles.borrar(id_rol)

