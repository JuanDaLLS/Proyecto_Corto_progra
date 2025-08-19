import os
from datetime import datetime
from PROYECTO_1 import Ahorro

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def leer_numero(mensaje, porcentaje=False):
    while True:
        valor = input(f"{GREEN}{mensaje}{RESET}")
        if valor == "":
            return 0
        try:
            numero = float(valor)
            return numero / 100 if porcentaje else numero
        except:
            print("Entrada inválida, intente de nuevo.")

def mostrar_menu():
    limpiar_consola()
    print(f"{RED}========== MENÚ PRINCIPAL =========={RESET}")
    print(f"{RED}Fecha: {obtener_fecha_actual()}{RESET}")
    print(f"{RED}{'-'*40}{RESET}\n")
    print("1. Instrucciones de uso")
    print("2. Empezar a ahorrar (definir plan)")
    print("3. Ver proyección de ahorro")
    print("4. Ver avances mes a mes")
    print("5. Salir")

def interpretar_opcion(entrada):
    e = entrada.strip().lower()
    return {
        "1": "1", "uno": "1",
        "2": "2", "dos": "2",
        "3": "3", "tres": "3",
        "4": "4", "cuatro": "4",
        "5": "5", "cinco": "5"
    }.get(e)

def menu():
    plan_definido = False
    plan = None

    while True:
        mostrar_menu()
        entrada = input(f"{GREEN}Seleccione una opción: {RESET}")
        opcion = interpretar_opcion(entrada)

        if opcion == "1":
            limpiar_consola()
            print(f"{RED}========== INSTRUCCIONES =========={RESET}")
            print(f"{RED}Fecha: {obtener_fecha_actual()}{RESET}")
            print(f"{RED}{'-'*40}{RESET}\n")
            print("- En la opción 2 define tu inversión mensual, los meses y la tasa de interés mensual.")
            print("- Opcional: puedes ingresar la inflación anual (si no, deja vacío).")
            print("- En la opción 3 verás tu proyección final.")
            print("- En la opción 4 verás la tabla de avances.")
            print(f"\n{RED}{'-'*40}{RESET}\n")
            input("Presione Enter para volver al menú...")

        elif opcion == "2":
            limpiar_consola()
            print(f"{RED}======= DEFINIR PLAN DE AHORRO ======={RESET}")
            print(f"{RED}Fecha: {obtener_fecha_actual()}{RESET}")
            print(f"{RED}{'-'*40}{RESET}\n")

            try:
                inversion_mensual = leer_numero("Ingrese su inversión mensual (Q): ")
                meses = int(leer_numero("Ingrese el número de meses: "))
                interes_mensual = leer_numero("Ingrese la tasa de interés MENSUAL (%): ", True)
                inflacion_anual = leer_numero("Inflación anual (%) [Enter = 0]: ", True)

                plan = Ahorro(inversion_mensual, meses, interes_mensual, inflacion_anual)
                plan_definido = True
                print(f"{GREEN}\nPlan guardado correctamente.{RESET}")
                print(f"{GREEN}Datos ingresados:{RESET}")
                print(f"{GREEN}- Inversión mensual: Q{inversion_mensual:,.2f}{RESET}")
                print(f"{GREEN}- Meses: {meses}{RESET}")
                print(f"{GREEN}- Tasa mensual: {interes_mensual*100:.4f}%{RESET}")
                print(f"{GREEN}- Inflación anual: {inflacion_anual*100:.2f}%{RESET}")
            except:
                print("\nError, verifique los datos ingresados.")
            print(f"\n{RED}{'-'*40}{RESET}\n")
            input("Presione Enter para volver al menú...")

        elif opcion == "3":
            limpiar_consola()
            print(f"{RED}===== PROYECCIÓN DE AHORRO ====={RESET}")
            print(f"{RED}Fecha: {obtener_fecha_actual()}{RESET}")
            print(f"{RED}{'-'*40}{RESET}\n")

            if not plan_definido:
                print("Primero debe definir su plan en la opción 2.")
            else:
                print(plan.resumen())
            print(f"\n{RED}{'-'*40}{RESET}\n")
            input("Presione Enter para volver al menú...")

        elif opcion == "4":
            limpiar_consola()
            print(f"{RED}===== AVANCES MES A MES ====={RESET}")
            print(f"{RED}Fecha: {obtener_fecha_actual()}{RESET}")
            print(f"{RED}{'-'*40}{RESET}\n")

            if not plan_definido:
                print("Primero debe definir su plan en la opción 2.")
            else:
                print(plan.tabla_avances())
            print(f"\n{RED}{'-'*40}{RESET}\n")
            input("Presione Enter para volver al menú...")

        elif opcion == "5":
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")
            print(f"\n{RED}{'-'*40}{RESET}\n")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()