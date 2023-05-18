'''
2-Escribe un programa que pida al usuario un número 
y calcule la suma de todos los números naturales del 1 hasta ese número.
'''
numero = int(input("Introduce un numero entero positivo: "))
suma = 0

for x in range(1, numero+1):
    suma += x

print(f"La suma de los números naturales del 1 al {numero} es: {suma}")


