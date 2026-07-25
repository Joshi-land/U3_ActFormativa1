print("""
---- REEMPLAZAR CARACTER ----

> Dada una cadena ingresar el caracter a reemplazar por uno nuevo

""")

def reemplazar(cadena,old,new):
    if len(old) !=1 or len(new) != 1:
        return cadena, 0
    resultado = ""
    changes =0
    for letra in cadena:
        if letra == old:
         resultado += new
         changes += 1
        else:
         resultado += letra
    return resultado, changes

cadena_in = input("\n> Ingrese una palabra: ")
chr_old = input("\n> Carácter a reemplazar: ")
chr_new = input("\n> Carácter nuevo: ")

if len(chr_old) != 1 or len(chr_new) != 1:
    print("\v<<<< DEBE INGRESAR UN SOLO CARÁCTER >>>>")
else:
    cadena_mod, num_change = reemplazar(cadena_in, chr_old, chr_new)
    cadena_mod2 = cadena_in.replace(chr_old, chr_new)
    print("\n> REEMPLAZO CON FUNCIÓN:", cadena_mod, " || CAMBIOS: ", num_change)
    print("\n> CON REPLACE: ",cadena_mod2)
    if cadena_mod == cadena_mod2:
        print("<<< CORRECTO >>>")