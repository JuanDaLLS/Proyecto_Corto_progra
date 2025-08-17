import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class Ahorro:

    def __init__(self, inversion_mensual: float, meses: int, interes_mensual: float, inflacion_anual: float = 4.5):
        if meses < 0: raise ValueError("Meses no puede ser negativo.")
        if interes_mensual <= -1: raise ValueError("La tasa mensual debe ser > -100%.")
        if inflacion_anual <= -1: raise ValueError("La inflación anual debe ser > -100%.")
        if inversion_mensual < 0: raise ValueError("La inversión mensual no puede ser negativa.")

        self.__inversion_mensual = float(inversion_mensual)
        self.__meses = int(meses)
        self.__interes = float(interes_mensual)       
        self.__inflacion_anual = float(inflacion_anual)
        self.__ahorro_total = 0.0                     

  

    
    def inflacion_mensual(self) -> float:
    
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

