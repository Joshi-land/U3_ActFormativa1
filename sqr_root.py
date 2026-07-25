print (""""
---- METODO NEWTON-RAPHSON ----

> Dado un número positivo se determinara su raíz cuadrada mediante el método Newton - Raphson
> Se comparara el resultado con el metodo math.sqrt para verificar
""")
import math

def root_newton(num, tolerancia=1e-10):
    if num < 0:
        raise ValueError("<<< RAÍZ NEGATIVA INDETERMINADA >>>")
    estimacion = num /2.0
    while True:
        new = 0.5 * (estimacion + num/estimacion)
        if abs(new-estimacion) < tolerancia:
            return new
        estimacion = new
try:
    num = float(input("\n> Ingrese un número: "))
    root1= math.sqrt(num)
    root2= root_newton(num)
    print(f"\n> MATH.SQRT: {root1} || METODO NEWTON: {root2:.10f}")
    if abs(root1-root2) < 1e-9:
        print("\n>>> RESULTADOS COINCIDEN <<<")
    else:
        print("\n Diferencia significativa")
except ValueError as e:
    print("\n>>> ERROR: ", e, "<<<")
