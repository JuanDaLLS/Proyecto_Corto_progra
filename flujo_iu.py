def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Instrucciones")
    print("2. Ingresar datos de ahorro")
    print("3. Ver proyección")
    print("4. Salir")

def flujo_principal():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == '4':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nFunción aún no implementada.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    flujo_principal()