print("""
<<<< ¿ES PALINDROMO? >>>>

- Dada una cadena de texto determinar si esta es un palindromo
- Eliminar espacios y mostrar la longitud de la cadena ya limpia

""")

def es_palindromo(cadena):
    cadena = cadena.lower()
    limpio =""
    for chrct in cadena:
        if chrct != " ":
            limpio += chrct
    return limpio == limpio[::-1], limpio

entrada = input("> Ingrese una frase/palabra: ")
result, cadena_limp= es_palindromo(entrada)
if result:
    print("\n--- ES UN PALINDROMO ---")
else:
    print("\n--- NO ES UN PALINDROMO ---")
print("\n> Longitud del texto: ",len(cadena_limp))
