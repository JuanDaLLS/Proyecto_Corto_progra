class Ahorro:
    def __init__(self, inversion_mensual, meses, tasa_inflacion, interes):
        self.__inversion_mensual = inversion_mensual
        self.__meses = meses
        self.__tasa_inflacion = tasa_inflacion
        self.__interes = interes
        self.__ahorro_total = 0

class InteresAnual(Ahorro):
    def __init__(self, TasaMensual):
        # Se evita el error de atributos que no existen por el momento
        self.__TasaMensual = TasaMensual

    def calcular_infacionAnual(self):
        return (1 + self.__TasaMensual) ** (1/12) - 1
    




    
