import os
from datetime import datetime
from PROYECTO_1 import Ahorro

def limpiar_consola(): os.system('cls' if os.name == 'nt' else 'clear')  # Limpia según  donde se ejecute

def obtener_fecha_actual(): return datetime.now().strftime("%d/%m/%Y %H:%M")  # Fecha legible

def leer_numero(mensaje, porcentaje=False):  # Entrada numérica, permite porcentaje
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

def menu(): # Menú principal del programa
    plan_definido = False
    plan = 0

    while True:
        limpiar_consola()
        print("----------------------------------------")
        print("SECCIÓN: MENÚ PRINCIPAL")
        print("Fecha:", obtener_fecha_actual())
        print("----------------------------------------\n")

        print("1. Instrucciones de uso")
        print("2. Empezar a ahorrar (definir plan)")
        print("3. Ver proyección de ahorro")
        print("4. Ver avances mes a mes")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            limpiar_consola()
            print("----------------------------------------")
            print("SECCIÓN: INSTRUCCIONES")
            print("Fecha:", obtener_fecha_actual())
            print("----------------------------------------\n")

            print("- En la opción 2 define tu inversión mensual, los meses y la tasa de interés mensual.")
            print("- Opcional: puedes ingresar la inflación anual (si no, deja vacío).")
            print("- En la opción 3 verás tu proyección final.")
            print("- En la opción 4 verás la tabla de avances.")
            input("\nPresione Enter para volver al menú...")

        elif opcion == "2":
            limpiar_consola()
            print("----------------------------------------")
            print("SECCIÓN: DEFINIR PLAN DE AHORRO")
            print("Fecha:", obtener_fecha_actual())
            print("----------------------------------------\n")

            try:
                inversion_mensual = leer_numero("Ingrese su inversión mensual (Q): ")
                meses = int(leer_numero("Ingrese el número de meses: "))
                interes_mensual = leer_numero("Ingrese la tasa de interés MENSUAL (%): ", True)
                inflacion_anual = leer_numero("Inflación anual (%) [Enter = 0]: ", True)

                plan = Ahorro(inversion_mensual, meses, interes_mensual, inflacion_anual)
                plan_definido = True
                print("\nPlan guardado correctamente.")
                print("Datos ingresados:")
                print(f"- Inversión mensual: Q{inversion_mensual}")
                print(f"- Meses: {meses}")
                print(f"- Tasa de interés mensual: {interes_mensual * 100}%")
                print(f"- Inflación anual: {inflacion_anual * 100}%")
            except:
                print("\nError, verifique los datos ingresados.")
            input("\nPresione Enter para volver al menú...")

        elif opcion == "3":
            limpiar_consola()
            print("----------------------------------------")
            print("SECCIÓN: PROYECCIÓN DE AHORRO")
            print("Fecha:", obtener_fecha_actual())
            print("----------------------------------------\n")

            if not plan_definido:
                print("Primero debe definir su plan en la opción 2.")
            else:
                print(plan.resumen(0.0))
            input("\nPresione Enter para volver al menú...")

        elif opcion == "4":
            limpiar_consola()
            print("----------------------------------------")
            print("SECCIÓN: AVANCES MES A MES")
            print("Fecha:", obtener_fecha_actual())
            print("----------------------------------------\n")

            if not plan_definido:
                print("Primero debe definir su plan en la opción 2.")
            else:
                print(plan.tabla_avances(0.0))
            input("\nPresione Enter para volver al menú...")

        elif opcion == "5":
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__": menu()  # Punto de entrada