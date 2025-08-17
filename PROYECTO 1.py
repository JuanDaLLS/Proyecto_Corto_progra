import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class Ahorro:
    def __init__(self, inversion_mensual: float, meses: int, interes_mensual: float, inflacion_anual: float = 0.0):
        if meses < 0: raise ValueError("Meses no puede ser negativo.")
        if interes_mensual <= -1: raise ValueError("La tasa mensual debe ser > -100%.")
        if inflacion_anual <= -1: raise ValueError("La inflación anual debe ser > -100%.")
        if inversion_mensual < 0: raise ValueError("La inversión mensual no puede ser negativa.")

        self.__inversion_mensual = float(inversion_mensual)
        self.__meses = int(meses)
        self.__interes = float(interes_mensual)       # i mensual en fracción (ej. 0.01 = 1%)
        self.__inflacion_anual = float(inflacion_anual)  # fracción anual (ej. 0.05 = 5%)
        self.__ahorro_total = 0.0

    def inflacion_mensual(self) -> float:
        # Convierte la inflación anual a mensual equivalente
        return (1 + self.__inflacion_anual)**(1/12) - 1

    def fv_nominal(self, pv: float = 0.0) -> float:
        i = self.__interes
        n = self.__meses
        PMT = self.__inversion_mensual
        if n == 0:
            return float(pv)
        if abs(i) < 1e-12:
            return float(pv) + PMT * n
        return float(pv) * (1 + i)**n + PMT * (((1 + i)**n - 1) / i)

    def fv_real(self, pv: float = 0.0) -> float:
        fv = self.fv_nominal(pv)
        pi_m = self.inflacion_mensual()
        n = self.__meses
        if abs(pi_m) < 1e-12:
            return fv
        return fv / ((1 + pi_m)**n)

    def resumen(self, pv: float = 0.0) -> str:
        fv_nom = self.fv_nominal(pv)
        fv_real = self.fv_real(pv)
        self.__ahorro_total = fv_nom
        return (
            f"Aporte mensual: Q{self.__inversion_mensual:,.2f}\n"
            f"Meses: {self.__meses}\n"
            f"Tasa mensual: {self.__interes*100:.4f}%\n"
            f"Inflación anual: {self.__inflacion_anual*100:.2f}%\n"
            f"FV nominal (Q de futuro): Q{fv_nom:,.2f}\n"
            f"FV real (Q de hoy): Q{fv_real:,.2f}"
        )

    def tabla_avances(self, pv: float = 0.0) -> str:
        i = self.__interes
        PMT = self.__inversion_mensual
        n = self.__meses
        pi_m = self.inflacion_mensual()

        saldo = float(pv)
        lineas = []
        encabezado = f"{'Mes':>3} | {'Interés':>12} | {'Aporte':>12} | {'Saldo nominal':>16} | {'Saldo real':>16}"
        sep = "-" * len(encabezado)
        lineas.append(encabezado)
        lineas.append(sep)

        for mes in range(1, n + 1):
            interes_mes = saldo * i if abs(i) >= 1e-12 else 0.0
            saldo += interes_mes
            saldo += PMT
            if abs(pi_m) < 1e-12:
                saldo_real = saldo
            else:
                saldo_real = saldo / ((1 + pi_m) ** mes)

            lineas.append(
                f"{mes:>3} | Q{interes_mes:>11,.2f} | Q{PMT:>11,.2f} | Q{saldo:>15,.2f} | Q{saldo_real:>15,.2f}"
            )

        return "\n".join(lineas)

def leer_float(mensaje: str, permitir_vacio: bool = False, por_ciento: bool = False, default: float = 0.0) -> float:
    while True:
        s = input(mensaje).strip()
        if s == "" and permitir_vacio:
            return default
        try:
            x = float(s)
            return x/100.0 if por_ciento else x
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def menu():
    plan = None
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

menu()
