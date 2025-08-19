PROGRAMA DE AHORRO — PROYECCION NOMINAL Y REAL

Este proyecto es una aplicación de consola que permite proyectar el ahorro con aportes mensuales, considerando la tasa de interés mensual y la inflación anual. 
El sistema cuenta con una clase principal llamada Ahorro, encargada de los cálculos, y un menú interactivo para el usuario final.

CARACTERISTICAS
- Calculo del Valor Futuro nominal con aportes mensuales.
- Ajuste por inflacion anual para obtener el Valor Futuro real.
- Generacion de una tabla con avances mes a mes (interes, aporte, saldo nominal y saldo real).
- Validaciones de entrada para evitar datos invalidos.
- Interfaz en consola con fecha y hora.

REQUISITOS
- Python 3.8 o superior
- No necesita librerias adicionales
- Opcional en Windows: instalar colorama si los colores no se muestran correctamente

EJEMPLO DE TABLA DE AVANCES

Mes | Interes |  Aporte  | Saldo nominal | Saldo real
------------------------------------------------------
  1 |   5.00  |  500.00  |       505.00  |     503.35
  2 |  10.05  |  500.00  |      1015.05  |    1009.14
  3 |  15.15  |  500.00  |      1530.20  |    1519.93
  4 |  20.30  |  500.00  |      2050.50  |    2035.78
  5 |  25.51  |  500.00  |      2576.01  |    2556.76
  6 |  30.76  |  500.00  |      3106.77  |    3082.93

USO
1. Instrucciones de uso
2. Empezar a ahorrar (definir plan)
3. Ver proyeccion de ahorro
4. Ver avances mes a mes
5. Salir

NOTAS
- Los datos deben ingresarse con punto decimal (ejemplo: 1.25 para 1.25%).
- Si se deja vacio un campo que lo permita, se tomara como cero.
- La inflacion ingresada debe ser anual, el sistema la convierte a mensual.
- La tasa de interes solicitada debe ser mensual.
