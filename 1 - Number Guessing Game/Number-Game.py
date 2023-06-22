import random as r
aleatorio = r.randint(0, 11)
continuar = True

while continuar:
    num = int(input("Ingrese un numeroentre 1 y 10: "))
    if num > aleatorio: 
        print("Mas grande")
    elif num < aleatorio: 
        print("Mas pequeño") 
    else: 
        print("Acertaste!!!")
        continuar = False

print("Fin del Juego")
    