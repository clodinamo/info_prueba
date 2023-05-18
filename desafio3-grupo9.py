from random import randint


print("Bienvenido al juego de adivine el numero!")

nombre_usuario: str = input("Ingrese su nombre: ")
cantidad_intentos: int = 8

print(f"Debe adivinar un numero entre el 1 y el 100, tiene {cantidad_intentos} intentos")

numero_secreto: int = randint(1, 100)

while(True):
    numero_usuario: str = input("Ingrese un numero: ")

    if numero_usuario.isdigit():
        numero = int(numero_usuario)

        if 1 <= numero <= 100:
            if numero < numero_secreto:
                print("El numero a adivinar es mayor")
            elif numero > numero_secreto:
                print("El numero a adivinar es menor")
            else:
                print(f"Ganaste el juego cuando te quedaban {cantidad_intentos} intentos")
                break
            cantidad_intentos -= 1
            
            if cantidad_intentos == 0:
                print(f"Game Over. El numero secreto era {numero_secreto}")
                break
            
            print(f"Te quedan {cantidad_intentos} intentos")


        else:
            print("El numero debe ser entre 1 y 100")
            input()

    else:
        print("Solo se permiten numeros...")
        input()


print("Fin del programa")