# Cambio 4: se importa math para usar math.pow en vez de operador **
import math  

class Ahorro:
    """Clase para modelar un plan de ahorro con interés compuesto e inflación."""  # Cambio 14: se agrega docstring general

    def _init_(self, inversion_mensual: float, meses: int, interes_mensual: float, inflacion_anual: float = 0.0):
        if not isinstance(meses, int) or meses <= 0:
            raise ValueError("Meses debe ser un entero positivo.")
        if interes_mensual <= -1:
            raise ValueError("La tasa mensual debe ser > -100%.")
        if inflacion_anual <= -1:
            raise ValueError("La inflación anual debe ser > -100%.")
        if inversion_mensual < 0:
            raise ValueError("La inversión mensual no puede ser negativa.")
        if inversion_mensual == 0:  # Cambio 1: no permitir aportes de 0
            raise ValueError("La inversión mensual no puede ser cero.")

        self.__inversion_mensual = float(inversion_mensual)
        self.__meses = int(meses)
        self.__interes = float(interes_mensual)
        self.__inflacion_anual = float(inflacion_anual)
        self.__ahorro_total = 0.0

        # Cambio 2: redondear valores internos para evitar errores de precisión
        self._inversion_mensual = round(self._inversion_mensual, 2)
        self._interes = round(self._interes, 6)
        self._inflacion_anual = round(self._inflacion_anual, 6)

    def inflacion_mensual(self) -> float:
        """Calcula la inflación mensual equivalente a la inflación anual."""  # Cambio 8: se agrega docstring
        # Cambio 4: usar math.pow en vez de operador ** para mayor claridad
        return math.pow(1 + self.__inflacion_anual, 1/12) - 1

    def fv_nominal(self, pv=0):
        """Calcula el valor futuro nominal del ahorro."""  # Cambio 8: docstring
        pv = float(pv)  # Cambio 3: asegurar que pv sea float
        i = self.__interes
        n = self.__meses
        pago = self.__inversion_mensual

        if n == 0:
            return pv
        if abs(i) < 1e-12:  # Cambio 5: tolerancia en vez de i == 0
            return pv + pago * n
        return pv * (1 + i) ** n + pago * (((1 + i) ** n - 1) / i)

    def fv_real(self, pv=0):
        """Calcula el valor futuro real ajustado por inflación."""  # Cambio 8: docstring
        pv = float(pv)  # Cambio 6: asegurar que pv sea float
        fv = self.fv_nominal(pv)
        pi_m = self.inflacion_mensual()
        n = self.__meses

        if abs(pi_m) < 1e-12:  # Cambio 7: usar tolerancia en vez de pi_m == 0
            return fv
        return fv / ((1 + pi_m) ** n)

    def resumen(self, pv: float = 0.0) -> str:
        """Genera un resumen del plan de ahorro."""  # Cambio 8: docstring
        pv = float(pv)  # Cambio 8 extra: convertir pv a float
        fv_nom = self.fv_nominal(pv)
        fv_real = self.fv_real(pv)
        self.__ahorro_total = fv_nom

        return (
            f"Aporte mensual: Q{self.__inversion_mensual:,.2f}\n"  # Cambio 9: usar separador de miles
            f"Meses: {self.__meses}\n"
            f"Tasa mensual: {self.__interes * 100:.2f}%\n"  # Cambio 9: ajustar a 2 decimales
            f"Inflación anual: {self.__inflacion_anual * 100:.2f}%\n"
            f"FV nominal (Q de futuro): Q{fv_nom:,.2f}\n"
            f"FV real (Q de hoy): Q{fv_real:,.2f}"
        )

    def tabla_avances(self, pv: float = 0.0) -> str:
        """Genera una tabla mes a mes mostrando el avance del ahorro nominal y real."""  # Cambio 15: docstring
        pv = float(pv)  # Cambio 10: asegurar que pv sea float
        i = self.__interes
        PMT = self.__inversion_mensual
        n = self.__meses
        pi_m = self.inflacion_mensual()

        saldo = float(pv)
        lineas = []
        # Cambio 13: encabezado más descriptivo
        encabezado = f"{'Mes':>3} | {'Interés ganado':>15} | {'Aporte':>12} | {'Saldo nominal':>16} | {'Saldo real':>16}"
        sep = "-" * len(encabezado)
        lineas.append(encabezado)
        lineas.append(sep)

        for mes in range(1, n + 1):
            interes_mes = saldo * i if abs(i) >= 1e-12 else 0.0
            saldo += interes_mes
            saldo += PMT
            if saldo < 0:  # Cambio 11: asegurar que el saldo nunca sea negativo
                saldo = 0
            saldo_real = saldo if abs(pi_m) < 1e-12 else saldo / ((1 + pi_m) ** mes)  # Cambio 12: usar abs(pi_m)

            lineas.append(
                f"{mes:>3} | Q{interes_mes:>14,.2f} | Q{PMT:>11,.2f} | Q{saldo:>15,.2f} | Q{saldo_real:>15,.2f}"
            )

        lineas.append(sep)  # Cambio 15 extra: línea de cierre en la tabla
        return "\n".join(lineas)



import os
from datetime import datetime


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