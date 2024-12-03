from modulo.cabina import Cabina

def menu_cabina():
    """
    Submenú para gestionar las cabinas. Este menú permite al usuario seleccionar
    una opción para registrar, modificar, listar, desactivar cabinas o volver al menú principal.
    """
    while True:
        print("\n--- Gestión de Cabinas ---")
        print("1. Registrar Cabina")
        print("2. Modificar Cabina")
        print("3. Listar Cabinas")
        print("4. Listar Cabinas por capacidad")
        print("5. Desactivar Cabina")
        print("6. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            registrar_cabina_menu()
        elif opcion == "2":
            modificar_cabina_menu()
        elif opcion == "3":
            Cabina.listar()
        elif opcion == "4":
            while True:
                try:
                    capacidad = int(input("Capacidad de la cabina: "))
                    if capacidad <= 0:
                        print("La capacidad debe ser mayor que 0.")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido para la capacidad.")
            Cabina.listar_para(capacidad)
        elif opcion == "5":
            desactivar_cabina_menu()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

def registrar_cabina_menu():
    """
    Función para registrar una nueva cabina.
    Realiza validaciones sobre el número de cabina, capacidad, tipo, y precio por noche antes de registrar la cabina.
    """
    print("\n--- Registrar Cabina ---")
    
    while True:
        numero_cabina = input("Número de la cabina: ")
        if not numero_cabina.isalnum() or len(numero_cabina) > 20:
            print("Número de cabina inválido. Debe ser una cadena alfanumérica con un máximo de 20 caracteres.")
        else:
            break

    while True:
        try:
            capacidad = int(input("Capacidad de la cabina: "))
            if capacidad <= 0:
                print("La capacidad debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para la capacidad.")

    tipos_validos = ['estándar', 'premium', 'suite']
    while True:
        tipo = input("Tipo de cabina (estándar, premium, suite): ").lower()
        if tipo not in tipos_validos:
            print(f"Tipo inválido. Debe ser uno de los siguientes: {', '.join(tipos_validos)}.")
        else:
            break

    while True:
        try:
            precio_noche = float(input("Precio por noche: "))
            if precio_noche <= 0:
                print("El precio por noche debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el precio por noche.")

    Cabina.registrar(numero_cabina, capacidad, tipo, precio_noche)

def modificar_cabina_menu():
    """
    Función para modificar una cabina existente. Permite cambiar los valores del número de cabina, capacidad, 
    tipo, estado y precio por noche, con la opción de dejar en blanco los campos que no desee modificar.
    """
    print("\n--- Modificar Cabina ---")
    
    while True:
        try:
            id_cabina = int(input("ID de la cabina a modificar: "))
            if id_cabina <= 0:
                print("El ID de la cabina debe ser un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido para el ID de la cabina.")
    
    print("Deja en blanco los campos que no deseas modificar.")

    numero_cabina = input("Nuevo número de la cabina: ")
    if numero_cabina and (not numero_cabina.isalnum() or len(numero_cabina) > 20):
        print("Número de cabina inválido. Debe ser una cadena alfanumérica con un máximo de 20 caracteres.")
        numero_cabina = None

    while True:
        capacidad = input("Nueva capacidad de la cabina: ")
        if capacidad:
            try:
                capacidad = int(capacidad)
                if capacidad <= 0:
                    print("La capacidad debe ser mayor que 0.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para la capacidad.")
        else:
            break

    tipos_validos = ['estándar', 'premium', 'suite']
    while True:
        tipo = input("Nuevo tipo de cabina (estándar, premium, suite): ").lower()
        if tipo and tipo not in tipos_validos:
            print(f"Tipo inválido. Debe ser uno de los siguientes: {', '.join(tipos_validos)}.")
        else:
            break

    estados_validos = ['disponible', 'ocupada', 'mantenimiento']
    while True:
        estado = input("Nuevo estado de la cabina (disponible, ocupada, mantenimiento): ").lower()
        if estado and estado not in estados_validos:
            print(f"Estado inválido. Debe ser uno de los siguientes: {', '.join(estados_validos)}.")
        else:
            break

    while True:
        precio_noche = input("Nuevo precio por noche: ")
        if precio_noche:
            try:
                precio_noche = float(precio_noche)
                if precio_noche <= 0:
                    print("El precio por noche debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el precio por noche.")
        else:
            break

    Cabina.modificar(id_cabina, numero_cabina, capacidad, tipo, estado, precio_noche)

def desactivar_cabina_menu():
    """
    Función para desactivar una cabina.
    Solicita el ID de la cabina a desactivar y llama a la función `Cabina.desactivar()` para actualizar su estado.
    """
    print("\n--- Desactivar Cabina ---")
    id_cabina = int(input("ID de la cabina a desactivar: "))
    Cabina.desactivar(id_cabina)

