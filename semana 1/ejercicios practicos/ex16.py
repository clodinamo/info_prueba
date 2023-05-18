peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en mt: '))

imc = peso / (altura**2)

print(f'Su Indice de Masa Corporal IMC es: {imc}')
