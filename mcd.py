
import math

print("""
---- CALCULAR MCD ----

> Dados dos números determincar su MCD con una función y comparar el resultado con la función built - in de math

""")

def mcd(num_a,num_b):
    num_a=abs(num_a)
    num_b=abs(num_b)
    if num_a==0 and num_b==0:
        return 0 
    while num_b != 0:
        num_a,num_b = num_b, num_a%num_b
    return num_a

num_1 = int(input("> Ingrese el primer número: "))
num_2= int(input("> Ingrese el segundo número: "))

resultado = mcd(num_1,num_2)
resultado_funct=math.gcd(num_1,num_2)

print("> MCD - Calculado: ", resultado)
print("> MCD - Calculado con math.gcd: ", resultado_funct)

print("\n > Los resultados coinciden "if resultado == resultado_funct else "Resultados no coinciden")
if num_1 == 0 and num_2== 0:
    print ("\n <<< Ambos números son 0 >>>")
else:
    print("<<< FIN >>>")