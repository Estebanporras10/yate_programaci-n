from menu.menu_cabina import menu_cabina
from menu.menu_roles import menu_roles
from menu.menu_trabajador import menu_trabajadores
from menu.menu_pasajeros import menu_pasajero
from menu.menu_servicios import menu_servicio

def main():
    """
    Muestra el menú principal y ejecuta las opciones seleccionadas.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Control de cabinas")
        print("2. Mantenimiento de roles")
        print("3. Mantenimiento de trabajadores")
        print("4. Registro de pasajeros")
        print("5. Solicitud de servicios")
        print("6. Salir")
        opcion = input("\nSelecciona una opción (1-6): ")

        if opcion == "1":
            menu_cabina() 
        elif opcion == "2":
            menu_roles()
        elif opcion == "3":
            menu_trabajadores()
        elif opcion == "4":
            menu_pasajero()
        elif opcion == "5":
            menu_servicio()
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
