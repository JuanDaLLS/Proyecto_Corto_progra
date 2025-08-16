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
            input("\nPresione Enter para volver al menú...")
            
        elif opcion == '3':
            limpiar_consola()
            print("=== PROYECCIÓN ===")
            input("\nPresione Enter para volver al menú...")
            
        elif opcion == '4':
            print("\nSaliendo del programa...")
            break
            
        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

menu()

class Ahorro:
    def __init__ (self, inversion_mensual, meses, tasa_interes):
        self.inversion_mensual = inversion_mensual
        self.meses = meses
        self.tasa_interes = tasa_interes
