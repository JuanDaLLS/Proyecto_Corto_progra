import os
from PROYECTO_1 import Ahorro

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_numero(mensaje, porcentaje=False):
    while True:
        valor = input(mensaje)
        if valor == "":
            return 0
        try:
            numero = float(valor)
            if porcentaje:
                return numero / 100
            return numero
        except:
            print("Entrada inválida, intente de nuevo.")

def menu():
    plan_definido = False
    plan = 0  
    while True:
        limpiar_consola()
        print("=== PROGRAMA DE AHORRO ===")
        print("1. Instrucciones de uso")
        print("2. Empezar a ahorrar (definir plan)")
        print("3. Ver proyección de ahorro")
        print("4. Ver avances mes a mes")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            limpiar_consola()
            print("=== INSTRUCCIONES ===")
            print("- Opción 2: ingresa tu aporte mensual, meses y tasa mensual (%).")
            print("  Opcional: inflación anual (%) para ver el valor real.")
            print("- Opción 3: muestra tu proyección final nominal y real.")
            print("- Opción 4: muestra una tabla de avances mes a mes (con intereses y ajuste por inflación).")
            input("\nPresione Enter para volver al menú...")

        elif opcion == '2':
            limpiar_consola()
            print("=== DEFINIR PLAN DE AHORRO ===")
            try:
                inversion_mensual = leer_float("Ingrese su inversión mensual (Q): ", permitir_vacio=False)
                meses = int(leer_float("Ingrese el número de meses: ", permitir_vacio=False))
                interes_mensual = leer_float("Ingrese la tasa de interés MENSUAL (%): ", por_ciento=True)
                inflacion_anual = leer_float("Inflación anual (%) [Enter = 0]: ", permitir_vacio=True, por_ciento=True, default=0.0)
                plan = Ahorro(inversion_mensual, meses, interes_mensual, inflacion_anual)
                print("\nPlan guardado correctamente.")
            except Exception as e:
                print(f"\nError: {e}. Verifique los datos ingresados.")
            input("\nPresione Enter para volver al menú...")

        elif opcion == '3':
            limpiar_consola()
            print("=== PROYECCIÓN ===")
            if plan is None:
                print("Primero define tu plan en la opción 2.")
            else:
                print(plan.resumen(pv=0.0))
            input("\nPresione Enter para volver al menú...")

        elif opcion == '4':
            limpiar_consola()
            print("=== AVANCES MES A MES ===")
            if plan is None:
                print("Primero define tu plan en la opción 2.")
            else:
                print(plan.tabla_avances(pv=0.0))
            input("\nPresione Enter para volver al menú...")

        elif opcion == '5':
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()