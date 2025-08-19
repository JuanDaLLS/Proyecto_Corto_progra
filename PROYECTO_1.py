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