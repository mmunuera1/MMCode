#simulador de un bingo
import random
import time 

NUM_MIN = 1
NUM_MAX = 90
arrNum = list()

def generarArrayNum(): ############funcion donde crea los numeros del 1 al 30, simulando las bolas de un bingo
    for i in range(NUM_MAX):
        j = i+1
        arrNum.append(j)

def mostrarNumerosRandom():
    generarArrayNum()
    num_max = NUM_MAX-1
    num_min = NUM_MIN-1
    index = 1
    while(len(arrNum) != 0):
        randNum = random.randint(num_min, num_max)
        print(f"{arrNum[randNum]}")
        arrNum.pop(randNum)
        num_max -= 1
        index += 1
        time.sleep(0.2)

def ini():
    print("**********Bienvenido al bingo**************\n")
    res = input("¿Quieres jugar al bingo?(s/n)(exit para salir)")
    while True:
        if(res == 's'): 
            mostrarNumerosRandom();
            break
        elif(res == 'n'):
            break
        elif(res == "exit"):
            break
        else:
            res = input("Comando incorrecto...\n¿Quieres Jugar al bingo?(s/n)(exit para salir)")
    exit

ini()
        
    