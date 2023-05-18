# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Comprobamos si el número es múltiplo de 2 y de 3 a la vez
if numero % 2 == 0 and numero % 3 == 0:
    print(f"{numero} es múltiplo de 2 y de 3 a la vez")
else:
    print(f"{numero} no es múltiplo de 2 y de 3 a la vez")