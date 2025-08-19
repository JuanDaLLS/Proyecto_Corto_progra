# Proyecto_Corto_progra
Este es el repositorio con los commits de cada uno de los integrantes

Explicacion del sistema: 
Programa de Ahorro
CLASES: 

Ahorro
Esta clase sirve para simular un plan de ahorro mensual con intereses y también considerando la inflación.
El objetivo es calcular cuánto dinero se tendrá al final y mostrar una tabla con los avances cada mes

Métodos de AHORRO:
Constructor de la clase. ---> __init__(self, inversion_mensual, meses, interes_mensual, inflacion_anual=0)

VARIABLES: 
inversion_mensual:
cantidad de dinero que se aporta cada mes (pago).
meses: número de meses que durará el plan.
interes_mensual: tasa de interés aplicada cada mes (ejemplo: 0.02 = 2%).
inflacion_anual: tasa de inflación anual (opcional si no se coloca toma 0).
Valida que los datos no sean negativos y si hay un error, pone el valor en 0.

