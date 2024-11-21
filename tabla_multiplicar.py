TEXTO_INICIAL = "¿Que tabla de multiplicar quieres que te muestre? (pulse 's' para salir del programa)\n"

def ini():
    inputText = input(TEXTO_INICIAL)
    while(inputText != 's'):
        mostrarTabla(inputText)
        inputText = input(TEXTO_INICIAL)


def mostrarTabla(tabla):
    for i in range(11):
        multiplicador = int(tabla) * i
        print( f"{tabla}  *  {i}  =  {multiplicador}\n" )
    print("\n\n")

ini()