import random
import string

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    # Caracteres básicos: solo letras minúsculas
    caracteres = string.ascii_lowercase

    # Agregar caracteres según las preferencias del usuario
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ""
    for _ in range(longitud):
        contraseña += (random.choice(caracteres))
    return contraseña

def ini():
    longitud = int(input("¿De cuántos caracteres deseas la contraseña? (mínimo 6): "))
    while longitud < 6:
        print("La longitud minima es de 6 caracteres.")
        longitud = int(input("Por favor, ingresa una longitud valida: "))

    # Opciones de personalización
    incluir_mayusculas = input("¿Incluir mayusculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("¿Incluir numeros? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("¿Incluir simbolos? (s/n): ").strip().lower() == 's'

    contraseña_generada = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    print("\nTu contraseña generada es:")
    print(contraseña_generada)

ini()
