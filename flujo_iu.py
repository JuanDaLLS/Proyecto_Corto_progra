import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpiar_consola()  
        print("=== PROGRAMA DE AHORRO ===")
        print("1. Instrucciones de uso")
        print("2. Empezar a ahorrar")
        print("3. Ver proyección de ahorro")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            limpiar_consola()
            print("=== INSTRUCCIONES ===")
            print("1. Ingrese sus datos financieros...")
            print("2. Calcule su capacidad de ahorro...")
            input("\nPresione Enter para volver al menú...")
            
        elif opcion == '2':
            limpiar_consola()
            print("=== AHORRO ===")
            try:
                inversion_mensual = float(input("Ingrese su inversión mensual: "))
                meses = int(input("Ingrese el número de meses: "))
                interes = float(input("Ingrese la tasa de interés mensual: ")) / 100
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos.")
                input("Presione Enter para continuar...")
                continue
            input("\nPresione Enter para volver al menú...")
            
        elif opcion == '3':
            limpiar_consola()
            print("=== PROYECCIÓN ===")
            # No se imprime nada, pero no lanza errores
            input("\nPresione Enter para volver al menú...")
            
        elif opcion == '4':
            print("\nSaliendo del programa...")
            break
            
        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()