print ("""
---- CONTADOR DE CARACTERES ----

> Determinar el número de caracteres ingresados ya sea númerico o no

""")

def main():
    contador= 0 
    while True:
        entrada = input("> Ingrese un caracter: ")
        if entrada == " ":
            break
        try:
            if entrada.isdigit():
                entrada = str(entrada)
            print(entrada.upper())
            contador += 1
        except Exception as e:
            print("Error: ",e)
    print("\n>>> FIN <<<")
    print("\n> Caracteres ingresados: ", contador)
main()