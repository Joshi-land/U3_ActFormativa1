def es_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

print("""
<<<< ¿ES PRIMO? >>>>

- Dado un número se determinara si este es primo o no

""")

num =int(input("Ingrese un número: "))
if es_primo(num):
        print("El número es primo")
else:
        print("El número no es primo")