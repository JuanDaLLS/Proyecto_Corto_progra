class Ahorro:
    def __init__(self, inversion_mensual: float, meses: int, interes_mensual: float, inflacion_anual: float = 0.0):
        if meses < 0:
            raise ValueError("Meses no puede ser negativo.")
        if interes_mensual <= -1:
            raise ValueError("La tasa mensual debe ser > -100%.")
        if inflacion_anual <= -1:
            raise ValueError("La inflación anual debe ser > -100%.")
        if inversion_mensual < 0:
            raise ValueError("La inversión mensual no puede ser negativa.")

        self.__inversion_mensual = float(inversion_mensual)
        self.__meses = int(meses)
        self.__interes = float(interes_mensual)
        self.__inflacion_anual = float(inflacion_anual)
        self.__ahorro_total = 0.0

    def inflacion_mensual(self) -> float:
        return (1 + self.__inflacion_anual) ** (1/12) - 1

    def fv_nominal(self, pv=0):
        i = self.__interes
        n = self.__meses
        pago = self.__inversion_mensual

        if n == 0:
            return pv
        if i == 0:
            return pv + pago * n
        return pv * (1 + i) ** n + pago * (((1 + i) ** n - 1) / i)

    def fv_real(self, pv=0):
        fv = self.fv_nominal(pv)
        pi_m = self.inflacion_mensual()
        n = self.__meses

        if pi_m == 0:
            return fv
        return fv / ((1 + pi_m) ** n)

    def resumen(self, pv: float = 0.0) -> str:
        fv_nom = self.fv_nominal(pv)
        fv_real = self.fv_real(pv)
        self.__ahorro_total = fv_nom
        return (
            f"Aporte mensual: Q{self.__inversion_mensual:,.2f}\n"
            f"Meses: {self.__meses}\n"
            f"Tasa mensual: {self.__interes * 100:.4f}%\n"
            f"Inflación anual: {self.__inflacion_anual * 100:.2f}%\n"
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
            saldo_real = saldo if abs(pi_m) < 1e-12 else saldo / ((1 + pi_m) ** mes)

            lineas.append(
                f"{mes:>3} | Q{interes_mes:>11,.2f} | Q{PMT:>11,.2f} | Q{saldo:>15,.2f} | Q{saldo_real:>15,.2f}"
            )

        return "\n".join(lineas)