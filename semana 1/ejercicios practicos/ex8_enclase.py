'''
Crea un programa que pida al usuario el radio de un circulo 
y muestre su diametro, su circunsferencia y su area.
Supon que pi es aprox 3.14159
'''

pi = 3.14159
radio = float(input("Ingrese el radio del circulo: "))

diametro = radio * 2
circunferencia = 2 * pi * radio
area= pi * pow(radio,2) 

print(f"El diametro del círculo es: {diametro} ")
print(f"La circunferencia del círculo es: {circunferencia} ")
print(f"El área del círculo es: {area} ")
