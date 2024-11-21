import random

def ini():
    # Lista de palabras para el juego
    palabras = ["python", "programacion", "desarrollador", "tecnologia", "inteligencia"]
    palabra = random.choice(palabras) 
    letras_adivinadas = ["_"] * len(palabra)  
    intentos_restantes = 6  
    letras_usadas = set() 

    print("¡El Ahorcado!")
    print("Adivina la palabra antes de que se acaben los intentos.\n")

    while intentos_restantes > 0 and "_" in letras_adivinadas:
        print(f"Palabra: {' '.join(letras_adivinadas)}")
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
        
        letra = input("Ingresa una letra: ").lower()

        # Validación de entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una letra valida.\n")
            continue

        if letra in letras_usadas:
            print("Ya intentaste esa letra. ¡Intenta con otra!\n")
            continue

        letras_usadas.add(letra)  # Agregar la letra al conjunto de letras usadas

        if letra in palabra:
            print("¡Correcto! sigue asi.\n")
            for idx, char in enumerate(palabra):
                if char == letra:
                    letras_adivinadas[idx] = letra
        else:
            print("¡Fallaste! Prueba otra letra.\n")
            intentos_restantes -= 1

    # Final del juego
    if "_" not in letras_adivinadas:
        print(f"¡Enhorabuena! Adivinaste la palabra: {palabra}")
    else:
        print(f"¡Perdiste! La palabra era: {palabra}")
    print("¿Otro intento?\n")

# Ejecutar el juego
ini()
