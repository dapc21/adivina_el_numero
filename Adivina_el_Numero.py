from random import *

nombre = input("Dime cuál es tu nombre: ")
print(f"\nBueno, {nombre}, he pensado un número entre el 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

rango = range(1,101)
numeros = list(rango)
intentos = 0
respuesta = 0
sorteo = choice(numeros)

while intentos < 8:
    respuesta = int(input("Dime un número del 1 al 100: "))
    intentos += 1

    if respuesta not in rango:
        print("Tu número no es válido, debe estar entre 1 y 100.")
    elif respuesta < sorteo:
        print(f"El número {respuesta} es menor al número secreto.")
    elif respuesta > sorteo:
        print(f"El número {respuesta} es mayor al número secreto.")
    else:
        print(f"¡Has ganado! acertaste el número secreto en {intentos} intento(s).")
        break

else:
    print(f"\nLo siento, agotaste todas tus oportunidades.\nEl número secreto era el {sorteo}")