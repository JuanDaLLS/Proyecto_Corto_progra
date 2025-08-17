def mostrar_encabezado():
    print("")
    print("========================================")
    print(" CALCULADORA DE AHORRO FINANCIERO ")
    print("========================================")
    print("")

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Calcular ahorro mensual")
    print("2. Ver historial de cálculos")
    print("3. Salir")

def obtener_opcion():
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

def iniciar_flujo():
    mostrar_encabezado()
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "1":
            print("")
            print("[Función de cálculo aún no implementada]")
            print("")
        elif opcion == "2":
            print("")
            print("[Función de historial aún no implementada]")
            print("")
        elif opcion == "3":
            print("")
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            print("")
            break
        else:
            print("")
            print("Opción inválida. Intente de nuevo.")
            print("")

if __name__ == "__main__":
    iniciar_flujo()